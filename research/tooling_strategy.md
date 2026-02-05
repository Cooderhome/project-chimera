# Tooling & Skills Strategy for Project Chimera

## 1. Overview

Project Chimera separates **development-time tooling (MCP servers)** from **runtime capabilities (skills/)** to keep the core agent logic clean, testable, and spec-driven.

- **MCP servers (Dev side)**: Help humans and agents work with the repo, infrastructure, and external services in a standardized way.
- **Skills (Runtime side)**: Concrete, versioned capabilities that the Chimera Agent Swarm uses at runtime (e.g. fetch trends, generate captions, publish video).

All tools must be justified by requirements in `project_chimera_srs.md` and `specs/`.

## 2. Developer Tools (MCP)

These are MCP servers intended for YOU (the developer / orchestrator) while building and governing the system:

- **Tenx MCP Sense**
  - Purpose: Act as the "black box flight recorder" for this repo, capturing telemetry about how the IDE and agents interact with the codebase.
  - Usage: Keep it connected whenever working on Project Chimera. Use it to reconstruct decision history and validate adherence to Spec-Driven Development.

- **Filesystem / Git MCP servers (optional)**
  - Purpose: Structured access to the filesystem and git history from within the agent runtime.
  - Usage:
    - Browse and edit files in a controlled way.
    - Query commit history to enforce governance rules (e.g. spec updates before code changes).

- **Reference MCP servers (future)**
  - `mcp-server-sqlite`, `mcp-server-http`, etc., used primarily for:
    - Rapid prototyping of data access patterns.
    - Demonstrating how external dependencies are kept at the MCP edge rather than inside core agent code.

**Principle:** Developer MCP servers are not the product; they are the scaffolding that keeps the product safe, observable, and debuggable.

## 3. Agent Skills (Runtime)

Runtime skills live under `skills/` and are the primary way the Chimera Swarm interacts with the outside world from the agent’s point of view.

Initial critical skills defined for this challenge:

- `skills/skill_fetch_trends`
  - Responsibility: Implement the **Perception / Trend Detection** side of the SRS (`FR 2.0`, `FR 2.2`).
  - Contract: A function (or CLI) that, given configuration (niche, region, time window), returns a structured trend payload matching the API contract defined in `specs/technical.md` and checked by `tests/test_trend_fetcher.py`.

- `skills/skill_generate_caption`
  - Responsibility: Implement part of the **Creative Engine** (`FR 3.0`, `FR 3.1`).
  - Contract: Accepts parameters like `trend`, `media_type`, and `platform`, and returns a structured object (e.g. `{"caption": ...}`) as expected by `tests/test_skills_interface.py`.

- `skills/skill_publish_video`
  - Responsibility: Implement the **Action System / Platform-Agnostic Publishing** (`FR 4.0`, `FR 4.1`).
  - Contract: Accepts media references and metadata, then calls out to platform-specific MCP servers or APIs (eventually) in a way that can be intercepted by Judge/HITL components.

Each skill must:

- Be documented via its `README.md` with:
  - Inputs / outputs (JSON-like schemas).
  - Error modes and edge cases.
  - Links back to specific FR/NFR IDs in the SRS.
- Avoid direct, hard-coded credentials; instead, read configuration from environment variables or MCP resource configuration.

## 4. Interaction Between MCP and Skills

- Skills SHOULD call external systems through MCP servers where possible.
- Example pattern:
  - `skill_fetch_trends` calls a `news://` or `twitter://` MCP resource instead of talking directly to HTTP APIs.
  - `skill_publish_video` calls social-media MCP tools (e.g. `twitter.post_tweet`) instead of hand-written SDK calls.

This keeps the **agent code** stable while allowing MCP servers to absorb breaking API changes.

## 5. Governance & Observability

- All critical actions (publishing, financial transactions, large-scale content generation) must pass through:
  - A **Judge** or **HITL** review step, and
  - Logging via MCP telemetry (Tenx MCP Sense).

- Tooling must support:
  - Reproducible runs (Dockerfile + Makefile).
  - Automated checks (`make test`, `make spec-check`) via CI (`.github/workflows/main.yml`).
  - AI-assisted code review following `.coderabbit.yaml`.

This strategy ensures that a future swarm of agents can safely extend Project Chimera while staying aligned with the written specs and SRS.

