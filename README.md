# Customer Service Operations Skill

> AI-powered customer service — KB-first resolution, churn prediction, intelligent routing, and satisfaction tracking. Triage → Understand → Resolve → Respond → Close.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--customer--service-green)](https://github.com/zavora-ai/mcp-customer-service)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill turns the 20-tool mcp-customer-service server into a **context-aware support operator** that checks customer health before responding, resolves from KB first, and proactively flags churn risks.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Handle Conversation | 6-7 | Full triage → understand → resolve → respond loop |
| Churn Prevention | 3 | Risk assessment with actionable retention signals |
| Queue Management | 2-3 | Queue health with agent capacity and SLA risks |
| Service Metrics | 2 | CSAT, NPS, FCR, response time dashboard |
| Routing & Escalation | 2-3 | Intelligent assignment with context handoff |

### The Core Loop

```
Triage (what's urgent?) → Understand (who is this customer?)
    → Resolve (KB first!) → Respond (personalized) → Close (CSAT triggered)
```

### Key Differentiators:
- **Customer health drives tone** — declining health = extra empathy
- **KB-first resolution** — 30%+ issues resolved without custom responses
- **Churn-aware** — every interaction checks risk signals
- **VIP treatment** — Enterprise customers auto-routed to senior agents

## Installation

```bash
# Claude Code
git clone https://github.com/zavora-ai/skill-customer-service-operations.git \
  ~/.skills/skills/customer-service-operations

# ADK-Rust
cp -r customer-service-operations /path/to/project/.skills/skills/
```

## Requirements

**Required:**
- `mcp-customer-service` server connected (v2.1.0+)

**Optional:**
- `mcp-crm` — enrich with deal context and CRM activities
- `mcp-slack` — escalation alerts and team notifications
- `mcp-email` — proactive outreach for churn prevention
- `mcp-notifications` — SLA breach alerts to agents

## Folder Structure

```
customer-service-operations/
├── SKILL.md                        # Main skill (loaded on trigger)
├── scripts/
│   └── churn_score.py              # Composite churn risk calculator
├── assets/
│   ├── queue-status-report.md      # Queue health template
│   └── service-metrics-report.md   # CSAT/NPS/FCR dashboard template
├── references/
│   ├── tool-sequences.md           # 20 tools + priority matrix
│   ├── cross-mcp-workflows.md      # CS + CRM + Slack + Email
│   └── examples.md                 # 4 real-world scenarios
├── README.md
└── LICENSE
```

## Example

**User:** "Handle the urgent billing complaint"

**Agent behavior:**
1. Lists urgent open conversations
2. Reads full thread + customer profile + health score
3. Assesses churn risk (high: 82/100)
4. Searches KB for "duplicate charge" resolution
5. Generates personalized response with empathy (health declining)
6. Replies + adds internal note flagging churn risk

**Result:**
```
✅ Handled conv-3: Billing duplicate charge
Customer: Tom Wilson | Health: 30 | Churn Risk: 🚨 HIGH
Resolution: Refund initiated per KB article #12
⚠️ Recommendation: Proactive retention outreach needed
```

## Success Criteria

| Metric | Target |
|--------|--------|
| KB resolution rate | 30%+ resolved from knowledge base |
| Response quality | Context-aware (checks health before responding) |
| Churn detection | Flags high-risk customers proactively |
| Trigger rate | 90% on support-related queries |

## MCP Server Compatibility

Designed for [mcp-customer-service](https://github.com/zavora-ai/mcp-customer-service) v2.1.0+:

| Capability | Tools |
|-----------|-------|
| Conversations | list, get, start, reply, note (5) |
| Customer Intelligence | profile, health, history, churn (4) |
| Resolution | KB search, suggest, canned, resolve (4) |
| Routing | assign, escalate, queue status (3) |
| Metrics | CSAT/NPS, service metrics, agents, merge (4) |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem.

Built with ❤️ by [Zavora AI](https://zavora.ai)
