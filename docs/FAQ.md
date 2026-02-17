# Frequently Asked Questions (FAQ)

Common questions about the AI Project System, organized by category.

---

## Table of Contents

- [Philosophy & Approach](#philosophy--approach)
- [Practical Usage](#practical-usage)
- [Technical](#technical)
- [Adoption](#adoption)

---

## Philosophy & Approach

### Isn't this just waterfall?

**No.** This is a documentation-first approach designed for AI execution, not traditional waterfall.

**Key differences from waterfall:**
- **Specs are lightweight** — Not 100-page requirements documents. Epic specs are typically 1-3 pages of Markdown defining goals, deliverables, and success criteria.
- **Iteration is expected** — Specs can be updated based on findings. The difference is that updates are explicit and version-controlled, not verbal.
- **Execution is fast** — AI executes Epics in hours or days, not weeks or months.
- **Delivery is incremental** — Each Epic delivers working functionality, not a big-bang release.

**The similarity to waterfall:** Work is planned before execution. But planning ≠ waterfall. Planning enables autonomous AI execution.

### Why not just use Agile/Scrum/Kanban?

Agile/Scrum/Kanban assume **human-to-human communication**:
- Standups, retrospectives, and pair programming
- Verbal context shared in meetings
- Continuous back-and-forth during execution

AI agents need **explicit, written context**:
- No meetings or verbal communication
- Context must be in files, not memory
- Clear boundaries for when to start, stop, and deliver

The AI Project System is **Agile-compatible** — you can use Kanban boards, sprints, or continuous delivery. The difference is that execution units (Epics) are documented and bounded.

### Isn't this too much overhead?

**It depends on your project.**

**Yes, it's overhead if:**
- You're writing a single-file script
- You're doing pure exploratory coding
- You're prototyping something you'll throw away
- You're working alone on a project with no handoffs

**No, it's not overhead if:**
- You're building something you'll maintain
- You're collaborating with AI across multiple sessions
- Context loss has cost you time (re-explaining things to AI)
- Scope creep has caused problems
- You want repeatability and quality standards

**Trade-off:** You invest upfront in specs to get faster, more reliable AI execution. If you value predictability and context preservation, the overhead pays for itself.

### Can I use this for small projects?

**Yes, but with flexibility.**

Small projects can use:
- **Single Phase, single Milestone** — Skip the hierarchy if you don't need it.
- **Simplified specs** — Use the templates but keep specs brief.
- **Minimal governance** — Adopt only the parts you need (e.g., Epic specs + delivery notices, skip phases).

The system is **scalable down**. You don't need to use every feature for every project.

**Rule of thumb:** If your project has >3 distinct deliverables or >2 weeks of work, the structure helps. If it's smaller, use the templates as lightweight docs.

---

## Practical Usage

### How do I start a project?

**Three steps:**

1. **Read the Quick Start Guide**
   - [docs/QUICK-START.md](QUICK-START.md) walks you through creating your first Phase, Milestone, and Epic in ~30 minutes.

2. **Review the example project**
   - [examples/task-tracker-project/](../examples/task-tracker-project/) shows a complete project lifecycle (Phase P1, Milestones M1-M2, Epics E1.1-E2.4) with real specs, execution, and closure.

3. **Start with a small Epic**
   - Don't try to plan your entire project upfront. Create a Phase and Milestone, then write a spec for one Epic and execute it. Learn by doing.

**See also:**
- [docs/systems/start-a-project.md](systems/start-a-project.md) — Project initialization guide
- [docs/templates/README.md](templates/README.md) — Template usage instructions

### Do I need to use all the phases/milestones/epics?

**No. Use what fits your project.**

**Minimum viable structure:**
- **1 Phase** (your project)
- **1 Milestone** (a cohesive increment of work)
- **1+ Epics** (individual deliverables)

**When to add more structure:**
- **Multiple Phases:** If your project has distinct stages (e.g., Foundation → Features → Polish).
- **Multiple Milestones per Phase:** If a phase has multiple cohesive deliverables.
- **Multiple Epics per Milestone:** Most Milestones have 3-5 Epics.

**Guideline:** Structure follows work, not the other way around. If you have one big deliverable, use one Epic. If you have ten small deliverables, use ten Epics.

### Can I use this with [GitHub Projects / Jira / Linear]?

**Yes.** The AI Project System is **documentation-first**, not tool-dependent.

**Integration approaches:**
- **Markdown + GitHub Projects:** Create Epics as GitHub issues, link to Epic specs in `docs/phases/`.
- **Markdown + Jira:** Create Jira tickets for Epics, store specs in your repository's `docs/` folder.
- **Markdown + Linear:** Use Linear for task tracking, keep Epic specs in version control.

**Key principle:** Your project management tool tracks *status*. Your `docs/` folder tracks *specifications and decisions*. They're complementary.

**See also:**
- [docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md](systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md) — Integration guidance

### What if I don't use AI coding assistants?

**This system is designed for AI-assisted execution.** Without AI, you lose the primary value: autonomous execution from specs.

**But you can still use it for:**
- **Documentation standards** — The Phase/Milestone/Epic model works for human execution too.
- **Context preservation** — Explicit specs and decision records help human teams.
- **Delivery discipline** — The canonical happy path (spec → execute → review → accept → merge) prevents half-finished work.

**Bottom line:** The system works for humans, but it's optimized for AI agents. If you're not using AI, simpler approaches (e.g., README-driven development, ADRs) may be better.

### How do I handle bugs and hotfixes?

**Bugs during Epic execution:**
- Fix them as part of the Epic. Include in Definition of Done.

**Bugs after Epic closure:**
- **Small fixes:** Create a new Epic or handle via a patch PR (outside Epic workflow).
- **Significant bugs:** Create a new Epic with spec, Definition of Done, and delivery process.

**Hotfixes (production urgency):**
- Skip Epic process, fix directly, document afterward.
- Create a decision record explaining why process was bypassed.

**Guideline:** The Epic workflow is for planned work. Emergencies bypass process, but require post-hoc documentation.

### What if I have an idea during execution that's out of scope?

**Use an unplanned progress branch.**

During execution, you may encounter ideas, improvements, or refinements that add value but fall outside current Epic scope:
- Template improvements
- Governance clarifications  
- Documentation refinements
- Feature ideas for future work

**Don't break scope discipline.** Instead:

1. **Create an unplanned branch:**
   ```bash
   git checkout milestone/M<N>  # or other stable branch
   git checkout -b unplanned/<topic-slug>
   ```

2. **Commit your exploratory work** to the unplanned branch

3. **Continue your original Epic** without scope creep

4. **During planning**, HQ reviews unplanned branches and decides:
   - Create Epic to integrate the work
   - Defer for later
   - Discard explicitly

**Benefits:**
- Preserves creative insights without breaking execution discipline
- Creates feedback loop from execution → planning
- Stays within governance (no ungoverned commits)

**See also:**
- PROJECT-SYSTEM-GUIDELINES.md section 8A — Unplanned Progress Branches
- AI-OPERATING-GUIDELINES.md section 3.3 — HQ Planning and Unplanned Branches

---

## Technical

### Can I modify the governance documents?

**Yes, if you're using this system for your own projects.**

The governance documents ([PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md), [AI-OPERATING-GUIDELINES.md](AI-OPERATING-GUIDELINES.md)) are licensed under CC BY-SA 4.0, which allows modification with attribution.

**How to modify:**
1. **Fork or copy the repository** (this is your project's instance of the system).
2. **Update governance documents** to fit your needs (e.g., different branch naming, custom DoD requirements).
3. **Version your changes** — Update version numbers and effective dates.
4. **Maintain attribution** — Credit the original AI Project System per CC BY-SA 4.0.

**Important:** If you're contributing back to the `panchew/ai-project-system` repository, follow the original governance. Modifications apply to your own projects only.

**See also:**
- [docs/LICENSE](LICENSE) — CC BY-SA 4.0 license for documentation
- [CONTRIBUTING.md](../CONTRIBUTING.md) — How to contribute to the canonical repository

### What if my project doesn't fit the Phase-Milestone-Epic model?

**Adapt the model to your project.**

The Phase-Milestone-Epic hierarchy is **a default structure, not a rigid requirement**. You can:
- **Skip phases** — Use Milestones and Epics only.
- **Add levels** — Introduce sub-Epics or themes if needed.
- **Rename concepts** — Call them Releases/Sprints/Stories if that fits your team.

**What you shouldn't skip:**
- **Specs** — Document goals and deliverables before execution.
- **Definition of Done** — Define completion criteria explicitly.
- **Delivery process** — Spec → Execute → Review → Accept → Merge.

**The principles matter more than the names.** If your project needs different structure, keep the documentation-first, bounded-execution, explicit-review principles.

### Do I need to use Markdown?

**The system assumes Markdown**, but you can technically use other formats.

**Why Markdown:**
- Version control friendly (text-based, diffable)
- Readable in plain text and rendered (GitHub, GitLab, etc.)
- Widely supported by AI tools
- No proprietary formats or lock-in

**Alternatives:**
- **AsciiDoc** — Similar benefits, more features, less common.
- **ReStructuredText** — Python ecosystem standard, less AI-friendly.
- **Org-mode** — Emacs-native, powerful, niche.

**Not recommended:**
- **Word/Google Docs** — Not version-controllable, hard to diff.
- **Confluence/Notion** — Proprietary, AI agents can't access easily.

**Bottom line:** Markdown is strongly recommended. If you use something else, ensure it's text-based and version-controllable.

---

## Adoption

### How long does it take to set up?

**30 minutes to 2 hours**, depending on your starting point.

**Quickest path (30 minutes):**
1. Read [Quick Start Guide](QUICK-START.md) (10 min)
2. Create a Phase, Milestone, and Epic spec (15 min)
3. Execute one Epic with AI (5 min setup, AI does the work)

**Thorough path (2 hours):**
1. Read Quick Start + [PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md) (30 min)
2. Review [example project](../examples/task-tracker-project/) (30 min)
3. Set up your repository structure (15 min)
4. Create and execute your first Epic (45 min)

**After initial setup:** Creating new Epics takes 10-20 minutes (write spec, launch AI execution).

### Can I adopt this incrementally?

**Yes.** You don't need to restructure your entire project at once.

**Incremental adoption path:**

1. **Start with one Epic**
   - Pick a small deliverable, write an Epic spec, execute with AI.
   - No need to define Phases/Milestones yet.

2. **Add Milestones for cohesion**
   - Once you have 3-4 Epics, group them into a Milestone.

3. **Add Phases for structure**
   - If your project grows, introduce Phases to organize Milestones.

4. **Adopt governance gradually**
   - Start with Epic specs and Definition of Done.
   - Add review process, branch naming, and templates as needed.

**You can run this system alongside existing workflows.** Use it for new features while maintaining legacy processes for old code.

### Is there a CLI or automation tool?

**Not yet.** The system is currently manual (Markdown files + Git + AI chat).

**What exists:**
- Templates (copy-paste ready)
- Documentation
- Example project

**What doesn't exist (yet):**
- CLI to generate specs or validate structure
- GitHub Actions to enforce governance
- Automated Phase/Milestone/Epic creation

**Why manual?** The system is new. We're validating the model before building tooling.

**Future possibility:** If the community adopts this, tooling could be built. But for now, it's intentionally low-tech (Markdown + Git).

**Workaround:** Use your editor's snippet/template features to speed up file creation.

---

## Still have questions?

- **Check the documentation:** [docs/](.) has guides, templates, and examples.
- **Review the example project:** [examples/task-tracker-project/](../examples/task-tracker-project/) shows a complete lifecycle.
- **Open an issue:** [GitHub Issues](https://github.com/panchew/ai-project-system/issues) for questions, bugs, or suggestions.

**See also:**
- [CONTRIBUTING.md](../CONTRIBUTING.md) — How to contribute or report issues
- [PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md) — System structure and rules
- [AI-OPERATING-GUIDELINES.md](AI-OPERATING-GUIDELINES.md) — AI execution procedures
