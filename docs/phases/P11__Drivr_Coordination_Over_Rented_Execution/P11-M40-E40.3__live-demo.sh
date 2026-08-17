#!/usr/bin/env bash
# Live demonstration of the E40.3 surface, driven exactly as an operator would drive it:
# through bin/drivr-gate and curl. No pytest anywhere in this transcript.
set -u
cd /home/panchew/soft-dev/drivr

STATE=$(mktemp -d)/surface
FORGER=$(mktemp -d)/other-surface
PORT=8791
BASE="http://127.0.0.1:${PORT}"

say() { printf '\n\n===== %s =====\n' "$*"; }
run() { printf '\n$ %s\n' "$*"; eval "$@" 2>&1; }

say "0. VERSIONS AND LAYER"
run "python3 --version"
run "git -C /home/panchew/soft-dev/drivr log --oneline -1"
echo "state dir: ${STATE}"

say "1. START THE SURFACE (the daemon; a human runs this once)"
bin/drivr-gate --state-dir "${STATE}" serve --port "${PORT}" > /tmp/surface.log 2>&1 &
SERVER_PID=$!
trap 'kill ${SERVER_PID} 2>/dev/null' EXIT
sleep 1.5
cat /tmp/surface.log

say "2. HEADLESS-FIRST: THERE IS NOTHING TO LOOK AT"
run "curl -s -o /dev/null -w '%{http_code}  GET /\n'          ${BASE}/"
run "curl -s -o /dev/null -w '%{http_code}  GET /gates\n'     ${BASE}/gates"
run "curl -s -o /dev/null -w '%{http_code}  GET /queue\n'     ${BASE}/queue"
run "curl -s -o /dev/null -w '%{http_code}  GET /admin\n'     ${BASE}/admin"

say "3. MINT A LINK FOR ONE NAMED GATE (in-app; nothing is transmitted)"
LINK=$(bin/drivr-gate --state-dir "${STATE}" mint --gate 'merge-pr-211' --base "${BASE}")
echo "${LINK}"
echo
echo "and BEFORE any use, the authorization directory is:"
ls -la "${STATE}/authorizations" 2>&1 || echo "(does not exist — minting a link authorizes nothing)"

say "4. THE HUMAN OPENS IT — GET verifies and shows the gate. NOTHING IS SPENT."
run "curl -s -i '${LINK}'"
echo
echo "spend log after the GET:"
ls -la "${STATE}/spent" 2>&1 || echo "(does not exist — GET spent nothing)"

say "5. THE HUMAN CONFIRMS, ONCE — POST redeems"
TOKEN="${LINK#*t=}"
run "curl -s -i -X POST -d 't=${TOKEN}' ${BASE}/approve/merge-pr-211"

say "6. THE AUTHORIZATION ARTIFACT, MINTED IN-APP"
run "find ${STATE} -type f | sort"
echo
for f in "${STATE}"/authorizations/*.authorization.json; do
  echo "--- ${f} ---"; cat "${f}"
done
echo
echo "does the record contain the token itself?"
if ! ls "${STATE}"/authorizations/*.authorization.json >/dev/null 2>&1; then
  echo "INCONCLUSIVE — no authorization record exists to search"
elif grep -qF "${TOKEN}" "${STATE}"/authorizations/*.authorization.json; then
  echo "YES — a bearer credential leaked into the permanent record"
else
  echo "NO — the nonce identifies the link; the token is not retained"
fi

say "7. NEGATIVE TEST 1 of 4 — REUSE. The same link, a second time."
run "curl -s -i -X POST -d 't=${TOKEN}' ${BASE}/approve/merge-pr-211"

say "8. NEGATIVE TEST 2 of 4 — SIGNED. A link this surface did not mint."
FORGED=$(bin/drivr-gate --state-dir "${FORGER}" mint --gate 'merge-pr-211' --base "${BASE}")
echo "minted by a DIFFERENT surface (${FORGER}):"
echo "${FORGED}"
FORGED_TOKEN="${FORGED#*t=}"
run "curl -s -i -X POST -d 't=${FORGED_TOKEN}' ${BASE}/approve/merge-pr-211"

say "9. NEGATIVE TEST 3 of 4 — BOUND TO ONE GATE. A link for gate A, presented for gate B."
LINK_A=$(bin/drivr-gate --state-dir "${STATE}" mint --gate 'gate-A' --base "${BASE}")
TOKEN_A="${LINK_A#*t=}"
run "curl -s -i -X POST -d 't=${TOKEN_A}' ${BASE}/approve/gate-B"
echo
echo "and gate-A's link SURVIVED the attempt (a rejection must not burn a live link):"
run "curl -s -o /dev/null -w '%{http_code}\n' -X POST -d 't=${TOKEN_A}' ${BASE}/approve/gate-A"

say "10. NEGATIVE TEST 4 of 4 — EXPIRING. A 2-second link, used after 3 seconds. REAL CLOCK."
SHORT=$(bin/drivr-gate --state-dir "${STATE}" mint --gate 'short-lived' --ttl 2 --base "${BASE}")
SHORT_TOKEN="${SHORT#*t=}"
echo "minted at $(date -u +%H:%M:%SZ), ttl=2s"
echo "immediately (should be live):"
run "curl -s -o /dev/null -w '%{http_code}\n' '${SHORT}'"
echo "sleeping 3 seconds..."
sleep 3
echo "now, at $(date -u +%H:%M:%SZ):"
run "curl -s -i -X POST -d 't=${SHORT_TOKEN}' ${BASE}/approve/short-lived"

say "11. D4 — A CHAT REPLY, SENT TO THE ONLY INBOUND CHANNEL THAT EXISTS"
LIVE=$(bin/drivr-gate --state-dir "${STATE}" mint --gate 'merge-pr-212' --base "${BASE}")
echo "a VALID, LIVE, UNSPENT link exists for merge-pr-212 — so the surface has an"
echo "authorization it COULD mint. Now say yes in words instead:"
run "curl -s -i -X POST -d 'decision=approve&reply=yes, go ahead&message=LGTM, merge it' ${BASE}/approve/merge-pr-212"
run "curl -s -i -X POST -d 'approve=true&confirm=true' ${BASE}/approve/merge-pr-212"

say "12. AND PROSE RIDING ALONGSIDE A VALID TOKEN IS NOT READ EITHER"
LIVE_TOKEN="${LIVE#*t=}"
run "curl -s -i -X POST -d 'decision=reject&t=${LIVE_TOKEN}&note=do not do this' ${BASE}/approve/merge-pr-212"

say "13. FINAL STATE — every authorization this surface ever minted"
for f in "${STATE}"/authorizations/*.authorization.json; do
  echo "--- $(basename "${f}") ---"; cat "${f}"
done
echo
echo "count of authorizations: $(ls -1 "${STATE}"/authorizations/*.authorization.json | wc -l)"
echo "count of spent links:    $(ls -1 "${STATE}"/spent/*.spent | wc -l)"
echo
echo "signing key permissions:"
ls -l "${STATE}/signing.key"

say "14. THE SURFACE'S OWN ACCESS LOG (it keeps none — headless)"
cat /tmp/surface.log

kill ${SERVER_PID} 2>/dev/null
say "DONE"
