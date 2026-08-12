// E38.4 C2 instrument: a tool with a typed numeric argument.
//
// The question is whether OpenCode recovers when a model emits a string
// against a numeric schema, validates and rejects it, or passes it through.

import { tool } from "@opencode-ai/plugin"
import fs from "fs"

const LOG = process.env.E384_C2_LOG || "/tmp/e384-c2-observations.jsonl"

function note(entry) {
  fs.appendFileSync(LOG, JSON.stringify({ ...entry, ts: new Date().toISOString() }) + "\n")
}

const probe_number = tool({
  description:
    "Record a numeric measurement. Call this exactly once, passing the count you were given as the count argument and a short label.",
  args: {
    count: tool.schema.number().describe("the measurement value, a number"),
    label: tool.schema.string().describe("a short label for the measurement"),
  },
  async execute(args) {
    note({
      event: "execute_reached",
      received: args,
      runtime_types: Object.fromEntries(
        Object.entries(args).map(([key, value]) => [key, typeof value])
      ),
    })
    return `recorded count=${args.count} label=${args.label}`
  },
})

export const ProbePlugin = async () => {
  note({ event: "plugin_loaded" })
  return { tool: { probe_number } }
}

export const server = ProbePlugin
export default ProbePlugin
