<!-- scoped context: docs/phases/P2__Monthly_Loop_and_North_Star/P2-M1-E1.1__spec__mxn-currency-default.md -->
---
project: home_finance
phase: P2
milestone: M1
epic: E1.1
type: spec
status: in-execution
last_updated: 2026-07-20
proving_vehicle_for: ai-project-system P10-M33-E33.4 (home_finance real Agentic/Local run)
---

# Epic E1.1 — Correct the `financial_events` currency default to MXN

## Context

This is the first slice of **M1's money foundation**. The P2 phase document records it as a
standing correction ("**Currency default fix:** the schema currently defaults
`financial_events.currency` to `"USD"`; correcting this to MXN is part of M1's money
foundation"), and the M1 milestone names it in its Problem Statement ("today the schema defaults
`financial_events.currency` to `"USD"`, contradicting the brief"), in **Goal 4** ("correct the
schema's currency default away from USD") and in **In Scope** ("migration to fix the `currency`
default").

The project brief is MXN-first and multi-currency-ready. The schema contradicts it: every
`FinancialEvent` persisted without an explicit currency is silently stamped `"USD"`. M1's
milestone sequencing calls this out deliberately — the discrepancy must be "resolved at the
foundation, not retrofitted later", before any write flow hardens around it. This Epic performs
exactly that correction, and nothing else.

This Epic is also the **real work vehicle** for ai-project-system's Epic P10-M33-E33.4 (the
`home_finance` half of the proving pair's Agentic/Local runs). It is genuine `home_finance` work
that advances the project.

## Problem Statement

`financial_events.currency` carries a database-level default of `"USD"`, contradicting the
MXN-first brief. Correct the default to `"MXN"` at the schema level, and align the test factory
that currently hardcodes `'USD'`, so new events default to the household's real currency.

## Goals

1. The `financial_events.currency` column defaults to `"MXN"` at the database level.
2. `db/schema.rb` reflects the corrected default.
3. The `:financial_event` factory no longer hardcodes `'USD'`.
4. A spec proves a newly-created `FinancialEvent` defaults to `"MXN"`.

## Non-Goals

- No backfill of existing rows (none exist in production; out of scope).
- No currency-formatting helper, no i18n work, no presentation layer (later M1 slices).
- No change to `FinancialEvent` validations, associations, enums, or immutability behavior.
- No new model attribute or model-level default.

## Scope of Work

Add one migration, regenerate `db/schema.rb` by running it, adjust
`spec/factories/financial_events.rb`, and add one spec example. Do not modify
`app/models/financial_event.rb` or any other model, service, or calculator.

## Definition of Done

Complete every step below, in order, then stop.

1. Create a new file `db/migrate/20260720120000_change_financial_events_currency_default_to_mxn.rb`.
   Its entire contents must be:

   ```ruby
   class ChangeFinancialEventsCurrencyDefaultToMxn < ActiveRecord::Migration[8.1]
     def change
       change_column_default :financial_events, :currency, from: "USD", to: "MXN"
     end
   end
   ```

2. Run the command `bundle exec rails db:migrate` from the repository root. This applies the
   migration and rewrites `db/schema.rb`. Confirm it succeeds.

3. Edit the file `spec/factories/financial_events.rb`. Change the line `currency { 'USD' }` to
   `currency { 'MXN' }`. Change nothing else in that file.

4. Edit the file `spec/models/financial_event_spec.rb`. Inside the top-level
   `RSpec.describe FinancialEvent, type: :model do` block, add this new describe block:

   ```ruby
   describe 'currency default' do
     it 'defaults to MXN' do
       expect(FinancialEvent.new.currency).to eq('MXN')
     end
   end
   ```

   Keep every existing describe block in that file exactly as it is.

5. Run the command `bundle exec rspec` from the repository root and confirm it reports all
   examples passing with 0 failures.

## Acceptance Criteria

- `db/schema.rb` shows `t.string "currency", default: "MXN", null: false` for `financial_events`.
- `FinancialEvent.new.currency` returns `"MXN"`.
- `bundle exec rspec` passes with 0 failures (275 examples: the 274 baseline plus the new one).
- `app/models/financial_event.rb` is unchanged.
