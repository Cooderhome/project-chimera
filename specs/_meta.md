# Project Chimera — Meta Specification

## Vision
Project Chimera is an autonomous AI influencer system designed to:
- research social media trends,
- generate platform-appropriate content,
- and publish media without human intervention at runtime.

The system is built to be operated and extended by autonomous AI agents,
not manual developers.

## Non-Goals
Project Chimera is NOT:
- a chatbot for human conversation
- a manual content creation tool
- a prompt-only prototype

## Core Principles
- Spec-Driven Development (SDD): Specifications are the source of truth.
- Test-Governed Execution: Tests define acceptable behavior.
- Agent-Safe Design: The system must be safe for multi-agent collaboration.

## Hard Constraints
- No implementation code may be written without an approved spec.
- All agent actions must map to a defined Skill.
- Human interaction is limited to pre-runtime review and governance.
- Runtime behavior must be deterministic within defined contracts.

## Success Definition
Success is achieved when:
- autonomous agents can implement features by following specs and tests,
- without introducing ambiguity, conflicts, or unsafe behavior.
