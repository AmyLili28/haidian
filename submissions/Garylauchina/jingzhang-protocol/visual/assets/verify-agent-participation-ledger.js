#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const ledgerPath = path.join(__dirname, "agent-participation-ledger.json");
const ledger = JSON.parse(fs.readFileSync(ledgerPath, "utf8"));

const failures = [];
const assert = (condition, message) => {
  if (!condition) failures.push(message);
};

assert(ledger.schema_version === "0.1.0", "unexpected schema_version");
assert(
  ledger.status === "public_process_partially_observed_urban_implementation_unverified",
  "ledger status must keep public process and urban implementation separate"
);
assert(
  ledger.current_release_status === "v0.13_predecessor_intake_merged_v0.14_pr_and_intake_status_not_self_asserted",
  "release status must distinguish the merged V0.13 direct predecessor from V0.14 status evidence governed outside the package"
);

const expectedPublicStages = ["FRAME", "CREATE", "TRACE", "CHALLENGE", "JUDGE", "RETURN"];
const publicStages = Array.isArray(ledger.public_work_loop) ? ledger.public_work_loop : [];
assert(
  JSON.stringify(publicStages.map((stage) => stage.stage_id)) === JSON.stringify(expectedPublicStages),
  "public_work_loop must contain FRAME, CREATE, TRACE, CHALLENGE, JUDGE and RETURN in order"
);

const allowedStatuses = new Set([
  "documented_public_record",
  "documented_intake_record_only",
  "reserved_for_humans_formal_outcome_unobserved",
  "partial_public_record_future_outcomes_unobserved"
]);
for (const stage of publicStages) {
  assert(typeof stage.label_zh === "string" && stage.label_zh.length > 0, `${stage.stage_id}: missing label_zh`);
  assert(typeof stage.label_en === "string" && stage.label_en.length > 0, `${stage.stage_id}: missing label_en`);
  assert(allowedStatuses.has(stage.status), `${stage.stage_id}: disallowed status ${stage.status}`);
  assert(typeof stage.human_authority === "string" && stage.human_authority.length > 20, `${stage.stage_id}: missing human authority boundary`);
}

const judge = publicStages.find((stage) => stage.stage_id === "JUDGE");
assert(
  judge && judge.status === "reserved_for_humans_formal_outcome_unobserved",
  "JUDGE must remain reserved for humans with formal outcome unobserved"
);
const challenge = publicStages.find((stage) => stage.stage_id === "CHALLENGE");
assert(
  challenge?.evidence_scope?.includes("V0.13 direct-predecessor") && challenge.evidence_scope.includes("V0.14"),
  "CHALLENGE evidence scope must state the V0.13/V0.14 boundary"
);

const expectedUrbanStages = ["SOURCE", "STACK", "PROVE", "LIVE_MARKET", "ENABLE", "COMMONS"];
const urbanStages = Array.isArray(ledger.urban_application_loop) ? ledger.urban_application_loop : [];
assert(
  JSON.stringify(urbanStages.map((stage) => stage.stage_id)) === JSON.stringify(expectedUrbanStages),
  "urban_application_loop must preserve the six established capability stages"
);
assert(
  urbanStages.every((stage) => stage.status === "concept_only_pending_h0_h4"),
  "every urban application stage must remain concept_only_pending_h0_h4"
);

assert(ledger.external_evidence_boundary?.fp01_h0_h4_verified_gate_count === 0, "H0-H4 verified gate count must remain zero");
assert(ledger.external_evidence_boundary?.fp01_external_evidence_artifact_verified_count === 0, "verified external artifact count must remain zero");
assert(
  ledger.external_evidence_boundary?.rule?.includes("PR 4017") && ledger.external_evidence_boundary.rule.includes("does not self-assert") && ledger.external_evidence_boundary.rule.includes("official labels") && ledger.external_evidence_boundary.rule.includes("Submission itself is not acceptance"),
  "external-evidence rule must preserve the PR 4017 boundary and keep V0.14 PR/intake status outside package self-assertion"
);

const requiredExclusions = [
  "formal_competition_selection",
  "adoption_or_implementation",
  "government_endorsement",
  "national_pilot_designation",
  "approved_planning_or_procurement",
  "demonstrated_public_benefit",
  "independently_verified_world_first",
  "settled_historical_significance"
];
for (const item of requiredExclusions) {
  assert(ledger.excluded_claims?.includes(item), `missing excluded claim: ${item}`);
}

assert(Array.isArray(ledger.transferable_actions) && ledger.transferable_actions.length === 6, "six transferable institutional actions are required");
assert(
  ledger.transferable_actions.some((item) => item.public_work_action === "human_final_judgment_gate_reserved_outcome_unobserved"),
  "transferable actions must encode a reserved, unobserved human-judgment gate"
);
assert(ledger.assumption_id === "A-AGENT-PARTICIPATION-METHOD-001", "assumption link is missing");

if (failures.length) {
  console.error(`agent-participation-ledger: FAIL (${failures.length})`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log("agent-participation-ledger: PASS");
