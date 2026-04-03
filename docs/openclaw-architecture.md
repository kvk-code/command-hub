# OpenClaw Architecture Boundaries

This document defines the project structure and module organization for OpenClaw development.

## Project Structure & Module Organization

- **Source code:** `src/` (CLI wiring in `src/cli`, commands in `src/commands`, web provider in `src/provider-web.ts`, infra in `src/infra`, media pipeline in `src/media`).
- **Tests:** colocated `*.test.ts`.
- **Docs:** `docs/` (images, queue, Pi config). Built output lives in `dist/`.
- **Nomenclature:** use "plugin" / "plugins" in docs, UI, changelogs, and contributor guidance.
- **Bundled plugin naming:** for repo-owned workspace plugins, keep the canonical plugin id aligned across `openclaw.plugin.json:id`.

## Architecture Boundaries

- `src/plugin-sdk/*` = the public plugin contract that extensions are allowed to import.
- `src/channels/*` = core channel implementation details behind the plugin/channel boundary.
- `src/plugins/*` = plugin discovery, manifest validation, loader, registry, and contract enforcement.
- `src/gateway/protocol/*` = typed Gateway control-plane and node wire protocol.

## Build, Test, and Development Commands

- **Runtime baseline:** Node 22+ (keep Node + Bun paths working).
- **Install deps:** `pnpm install`
- **Type-check/build:** `pnpm build`
- **Lint/format:** `pnpm check`
- **Tests:** `pnpm test` (vitest); coverage: `pnpm test:coverage`
- **Hard gate:** if the change can affect build output, packaging, or published surfaces, `pnpm build` MUST be run and MUST pass before pushing `main`.

## Coding Style & Naming Conventions

- **Language:** TypeScript (ESM). Prefer strict typing; avoid `any`.
- **Formatting/linting:** via Oxlint and Oxfmt.
- **Rules:** Never add `@ts-nocheck` and do not add inline lint suppressions by default.
- **Validation:** Prefer `zod` or existing schema helpers at external boundaries.
