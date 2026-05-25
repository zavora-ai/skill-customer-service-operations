# Customer Service Tool Sequences Reference

## Tool Inventory (mcp-customer-service, 20 tools)

### Conversations (5)
| Tool | Risk | Purpose |
|------|------|---------|
| `list_conversations` | read | Filter by status, priority, agent |
| `get_conversation` | read | Full thread with messages |
| `start_conversation` | write | Start new conversation |
| `reply_conversation` | external_write | Public reply to customer |
| `add_internal_note` | write | Internal note (not visible to customer) |

### Customer Intelligence (4)
| Tool | Risk | Purpose |
|------|------|---------|
| `get_customer_profile` | read | Plan, LTV, health, history |
| `get_customer_health` | read | Health score + contributing factors |
| `get_interaction_history` | read | All past conversations |
| `assess_churn_risk` | read | Churn prediction with signals |

### Resolution (4)
| Tool | Risk | Purpose |
|------|------|---------|
| `search_knowledge_base` | read | Find relevant help articles |
| `suggest_response` | read | AI-suggested reply based on context |
| `get_canned_responses` | read | Approved response templates |
| `resolve_conversation` | write | Mark resolved + trigger CSAT |

### Routing (3)
| Tool | Risk | Purpose |
|------|------|---------|
| `assign_agent` | write | Assign to agent or team |
| `escalate` | write | Escalate with reason |
| `get_queue_status` | read | Queue depth, wait times |

### Metrics (4)
| Tool | Risk | Purpose |
|------|------|---------|
| `get_satisfaction_scores` | read | CSAT, NPS, effort scores |
| `get_service_metrics` | read | Response time, FCR, volume |
| `list_agents` | read | Agent availability |
| `merge_conversations` | destructive | Merge duplicate conversations |

## Sequence: Full Conversation Handling (6-7 calls)

```
1. list_conversations(status: "open", priority: "urgent")
   → [{id: "conv-3", subject: "Billing overcharge", customer: "cust-4", priority: "urgent"}]

2. get_conversation(id: "conv-3")
   → {messages: [{from: "customer", body: "I was charged twice for my subscription!"}], status: "open"}

3. get_customer_profile(customer_id: "cust-4")
   → {name: "Tom Wilson", plan: "Free", health: 30, ltv: 0, tenure: "3 months"}

4. assess_churn_risk(customer_id: "cust-4")
   → {risk: "high", score: 82, signals: ["declining_health", "billing_complaint", "3_tickets_30_days"]}

5. search_knowledge_base(query: "duplicate charge billing")
   → [{title: "Duplicate Charge Resolution", id: "kb-12", relevance: 0.89}]

6. suggest_response(conversation_id: "conv-3")
   → "I'm sorry about the duplicate charge, Tom. I can see this happened due to [reason]. I've initiated a refund..."

7. reply_conversation(id: "conv-3", body: "personalized response based on suggestion", is_public: true)
```

## Sequence: Churn Risk Assessment (3 calls)

```
1. assess_churn_risk(customer_id: "cust-4")
   → {risk: "high", score: 82, signals: ["declining_usage", "negative_sentiment", "billing_complaints"]}

2. get_customer_profile(customer_id: "cust-4")
   → {plan: "Pro", ltv: 2400, health: 45, tenure: "18 months"}

3. get_interaction_history(customer_id: "cust-4")
   → [{date: "2025-01-15", subject: "Billing issue"}, {date: "2025-01-10", subject: "Feature missing"}, ...]
```

## Sequence: Queue Triage (3 calls)

```
1. get_queue_status()
   → {total_open: 23, urgent: 3, avg_wait: "12 min", sla_at_risk: 2}

2. list_conversations(status: "open", sort: "priority_desc")
   → Top conversations by priority

3. list_agents()
   → [{name: "Agent A", status: "available", load: 3}, {name: "Agent B", status: "busy", load: 7}]
```

## Customer Health Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Healthy | Standard support |
| 60-79 | Stable | Monitor, ensure quick resolution |
| 40-59 | At Risk | Priority handling, check churn signals |
| 20-39 | Critical | Escalate to retention team, proactive outreach |
| 0-19 | Churning | Immediate intervention, executive escalation |

## Response Priority Matrix

| Customer Plan | Health | Priority | Action |
|--------------|--------|----------|--------|
| Enterprise | Any | Highest | Senior agent, immediate response |
| Pro | < 50 | High | Priority queue, churn assessment |
| Pro | > 50 | Medium | Standard queue |
| Free | < 30 | Medium | Assess upgrade potential |
| Free | > 30 | Normal | Standard queue, KB-first |
