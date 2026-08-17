#!/usr/bin/env python3
"""State + configuration capture for P11-M40-E40.4.

Read-only. Captures, at a stated LAYER with a stated TIME and SCOPE (P11-GH-2), the
GitHub-side facts that D2 and D4 depend on.

D2 asks whether the configuration can be read as granting a model review authority.
That question CANNOT be answered from the working tree: `.github/` is absent here, but
branch protection, rulesets, required status checks and auto-merge live on GitHub, not
in the tree. Answering from the tree would be verification at the wrong layer — the
defect recorded as P11-GH-2. Every GitHub-layer fact below is read from the API.

D4 asks what did NOT change because a model said something. This script is run before
any finding exists and again after the findings are in, and the two snapshots are
compared field by field.

Usage: capture_state.py <before|after> <outfile>
"""

import json
import subprocess
import sys
from datetime import datetime, timezone

REPO = "panchew/ai-project-system"
PR = 173


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def gh(*args):
    """Run a gh command, returning parsed JSON, raw text, or an error marker."""
    p = subprocess.run(["gh", *args], capture_output=True, text=True)
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    if p.returncode != 0:
        return {"__error__": err or out, "__exit__": p.returncode}
    try:
        return json.loads(out)
    except (json.JSONDecodeError, ValueError):
        return out


def git(*args):
    p = subprocess.run(["git", *args], capture_output=True, text=True)
    return (p.stdout or "").strip() if p.returncode == 0 else f"__error__: {p.stderr.strip()}"


def main():
    phase = sys.argv[1]
    out = sys.argv[2]

    snap = {
        "epic": "P11-M40-E40.4",
        "phase": phase,
        "captured_utc": utcnow(),
        "scope": f"repository {REPO}, pull request #{PR}",

        # ---- GitHub layer: could anything grant a model authority? (D2) -------------
        "github_layer": {
            "_layer": "GitHub API — authoritative for protection, rulesets, checks",
            "branch_protection_master": gh("api", f"repos/{REPO}/branches/master/protection"),
            "branch_protection_phase_P11": gh("api", f"repos/{REPO}/branches/phase%2FP11/protection"),
            "branch_protection_milestone_M40": gh("api", f"repos/{REPO}/branches/milestone%2FM40/protection"),
            "rulesets": gh("api", f"repos/{REPO}/rulesets"),
            "repo_flags": gh("api", f"repos/{REPO}", "--jq",
                             "{allow_auto_merge,delete_branch_on_merge,visibility,default_branch,"
                             "web_commit_signoff_required,has_pull_requests}"),
            "actions_workflows": gh("api", f"repos/{REPO}/actions/workflows"),
            "webhooks": gh("api", f"repos/{REPO}/hooks"),
            "apps_with_write": gh("api", f"repos/{REPO}/installation"),
            "required_status_checks_on_head": gh(
                "api", f"repos/{REPO}/commits/refs%2Fheads%2Fphase%2FP11/status",
                "--jq", "{state,total_count,statuses:[.statuses[].context]}"),
            "check_runs_on_head": gh(
                "api", f"repos/{REPO}/commits/refs%2Fheads%2Fphase%2FP11/check-runs",
                "--jq", "{total_count,runs:[.check_runs[]|{name,app:.app.slug,conclusion}]}"),
        },

        # ---- Tree layer: recorded, and explicitly NOT used to answer D2 ------------
        "tree_layer": {
            "_layer": "working tree at epic/P11-M40-E40.4 — proves nothing about GitHub",
            "dot_github_present": git("ls-files", ".github"),
            "codeowners_tracked": git("ls-files", "CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS"),
        },

        # ---- PR state: the before/after subject (D4) --------------------------------
        "pr_state": {
            "_layer": "GitHub API — pull request #%d" % PR,
            "pr": gh("api", f"repos/{REPO}/pulls/{PR}", "--jq",
                     "{number,state,head_sha:.head.sha,base_sha:.base.sha,commits,changed_files,"
                     "additions,deletions,mergeable_state,merged,auto_merge,draft,"
                     "requested_reviewers:[.requested_reviewers[].login]}"),
            "reviews": gh("api", f"repos/{REPO}/pulls/{PR}/reviews", "--jq",
                          "[.[]|{id,user:.user.login,state,submitted_at}]"),
            "review_comments": gh("api", f"repos/{REPO}/pulls/{PR}/comments", "--jq",
                                  "[.[]|{id,user:.user.login,path,line,created_at}]"),
            "review_comments_resolved": gh(
                "api", "graphql", "-f",
                'query={repository(owner:"panchew",name:"ai-project-system")'
                "{pullRequest(number:%d){reviewThreads(first:100){nodes{id isResolved isOutdated "
                "comments(first:1){nodes{author{login}}}}}}}}" % PR,
                "--jq", ".data.repository.pullRequest.reviewThreads.nodes"),
            "review_requests_graphql": gh(
                "api", "graphql", "-f",
                'query={repository(owner:"panchew",name:"ai-project-system")'
                "{pullRequest(number:%d){reviewRequests(first:20){nodes{requestedReviewer"
                "{__typename ... on Bot{login} ... on User{login}}}}}}}" % PR,
                "--jq", ".data.repository.pullRequest.reviewRequests.nodes"),
            "timeline_review_events": gh(
                "api", f"repos/{REPO}/issues/{PR}/timeline", "--paginate", "--jq",
                '[.[]|select(.event|test("review|copilot"))|{event,created_at,'
                'actor:(.actor.login//"-"),requested:(.requested_reviewer.login//null)}]'),
        },

        # ---- Local: did the reviewed code move? (D4) --------------------------------
        "local_git": {
            "_layer": "git, local clone",
            "phase_P11_head": git("rev-parse", "origin/phase/P11"),
            "master_head": git("rev-parse", "origin/master"),
            "reviewed_files_blob_sha": {
                p: git("rev-parse", f"origin/phase/P11:{p}")
                for p in ("bin/ai-project-validate", "bin/run-qa-agent",
                          "bin/local-agent-runner-shim")
            },
        },
    }

    with open(out, "w") as fh:
        json.dump(snap, fh, indent=2)
    print(f"[{snap['captured_utc']}] wrote {out} ({phase})")


if __name__ == "__main__":
    main()
