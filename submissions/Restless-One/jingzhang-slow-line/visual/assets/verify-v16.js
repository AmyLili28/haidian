#!/usr/bin/env node
'use strict';

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const SOURCE = path.join(__dirname, 'v16-communication-audit.json');
const RECEIPT = path.join(__dirname, 'v16-verification.json');

function fail(message) {
  throw new Error(message);
}

function sha256(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

const audit = JSON.parse(fs.readFileSync(SOURCE, 'utf8'));
if (audit.package_version !== 'v1.6-communication-hierarchy') fail('unexpected package version');
if (!Array.isArray(audit.reader_layers) || audit.reader_layers.length !== 3) fail('three reader layers are required');
const layers = new Set(audit.reader_layers.map(item => item.layer_id));
for (const required of ['L1-30SEC', 'L2-3MIN', 'L3-PRO']) {
  if (!layers.has(required)) fail(`missing reader layer ${required}`);
}
const checkpoints = audit.bilingual_controlled_checkpoints;
if (!Array.isArray(checkpoints) || checkpoints.length !== 12) fail('twelve bilingual checkpoints are required');
if (new Set(checkpoints.map(item => item.checkpoint_id)).size !== checkpoints.length) fail('duplicate bilingual checkpoint id');
if (checkpoints.some(item => !item.zh || !item.en || !item.status)) fail('incomplete bilingual checkpoint');
if (audit.current_result.paired_checkpoint_count !== checkpoints.length) fail('paired checkpoint total mismatch');
if (audit.visual_text_floors_canvas_px.public_figure_body < 20) fail('public figure body floor below 20 canvas px');
if (audit.visual_text_floors_canvas_px.technical_companion_body < 10) fail('technical companion body floor below 10 canvas px');

for (const rel of [
  'proposal.md',
  'proposal.en.md',
  'visual/index.html',
  'visual/index.en.html',
  'assets/media/p0-execution-workbook.md'
]) {
  if (!fs.existsSync(path.join(ROOT, rel))) fail(`missing paired communication input ${rel}`);
}

const receipt = {
  schema_version: '1.0.0',
  verifier: 'verify-v16.js',
  source: 'visual/assets/v16-communication-audit.json',
  source_sha256: sha256(SOURCE),
  result: 'PASS',
  checked: {
    reader_layers: audit.reader_layers.length,
    bilingual_checkpoints: checkpoints.length,
    paired_checkpoints: checkpoints.filter(item => item.status).length,
    public_fixed_figures: audit.artifact_separation.public_fixed_figure_count,
    technical_companion_figures: audit.artifact_separation.technical_companion_figure_count,
    public_body_floor_canvas_px: audit.visual_text_floors_canvas_px.public_figure_body
  },
  boundary: audit.audit_boundary
};
fs.writeFileSync(RECEIPT, JSON.stringify(receipt, null, 2) + '\n');
process.stdout.write(JSON.stringify(receipt, null, 2) + '\n');
