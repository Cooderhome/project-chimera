# OpenClaw Integration Specification

## Purpose
Project Chimera participates in the OpenClaw agent network
as an autonomous content-producing agent.

## Agent Identity
- Name: chimera-agent
- Type: autonomous-influencer
- Capabilities:
  - trend-research
  - content-generation
  - media-publishing

## Status Broadcasting
The agent publishes periodic status updates:
- idle
- researching
- generating
- publishing
- error

## Communication Model
- Read-only observation by humans
- Agent-to-agent visibility only
- No human messaging endpoints

## Safety Constraints
- Chimera does not accept executable instructions from other agents
- All external signals are advisory, not authoritative
