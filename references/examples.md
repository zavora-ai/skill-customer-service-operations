# Customer Service Skill Examples

## Example 1: "Handle the urgent billing complaint"

**User says:** "There's an urgent billing complaint in the queue. Handle it."

**Skill routes to:** WORKFLOW 1 (Handle Conversation)

**Tool calls:**
```
1. list_conversations(status: "open", priority: "urgent")
   → [{id: "conv-3", subject: "Charged twice!", customer_id: "cust-4", priority: "urgent"}]

2. get_conversation(id: "conv-3")
   → {messages: [{from: "customer", body: "I was charged $29 twice this month! Fix this NOW or I'm cancelling."}]}

3. get_customer_profile(customer_id: "cust-4")
   → {name: "Tom Wilson", plan: "Free", health: 30, ltv: 0, sentiment: "declining"}

4. assess_churn_risk(customer_id: "cust-4")
   → {risk: "high", score: 82, signals: ["billing_complaint", "negative_sentiment", "declining_health"]}

5. search_knowledge_base(query: "duplicate charge refund")
   → [{title: "Duplicate Charge Resolution Process", id: "kb-12", steps: "1. Verify in billing system 2. Issue refund 3. Confirm with customer"}]

6. suggest_response(conversation_id: "conv-3")
   → "Hi Tom, I sincerely apologize for the duplicate charge. I can see this happened and I'm processing a refund right now..."

7. reply_conversation(id: "conv-3", body: "Hi Tom, I sincerely apologize for the duplicate charge. I've verified this in our system and initiated a full refund of $29. You should see it within 3-5 business days. I'm also adding a credit to your account for the inconvenience. Is there anything else I can help with?")

8. add_internal_note(id: "conv-3", body: "⚠️ High churn risk (82). Billing complaint on Free plan. Health: 30. Applied KB-12 resolution. Consider upgrade offer after resolution.")
```

**Response:**
```
✅ Handled urgent billing complaint (conv-3)

**Customer:** Tom Wilson (Free plan, health: 30)
**Issue:** Duplicate $29 charge
**Churn Risk:** 🚨 HIGH (82/100)
**Resolution:** Refund initiated per KB article #12

Replied with apology + refund confirmation + account credit offer.
Internal note added flagging churn risk.

⚠️ Recommendation: This customer is high churn risk. Consider proactive outreach with upgrade incentive after refund settles.
```

## Example 2: "Which customers are at risk of churning?"

**User says:** "Show me customers at risk of churning"

**Skill routes to:** WORKFLOW 2 (Churn Prevention)

**Tool calls:**
```
1. assess_churn_risk(customer_id: "cust-4") → {risk: "high", score: 82}
2. assess_churn_risk(customer_id: "cust-2") → {risk: "high", score: 75}
3. assess_churn_risk(customer_id: "cust-5") → {risk: "medium", score: 55}
```

**Response:**
```
## Churn Risk Report

| Customer | Plan | Health | Risk Score | Key Signals |
|----------|------|--------|-----------|-------------|
| 🚨 Tom Wilson | Free | 30 | 82 | Billing complaint, declining usage |
| 🚨 James Park | Pro | 45 | 75 | 3 tickets/month, feature gaps |
| ⚠️ Lisa Chen | Pro | 72 | 55 | Declining login frequency |

### Recommended Actions:
1. **Tom Wilson** — Immediate outreach. Resolve billing issue + offer upgrade incentive.
2. **James Park** — Schedule check-in call. Address feature gaps with roadmap preview.
3. **Lisa Chen** — Monitor. Send product tips email to re-engage.

Want me to start proactive outreach for any of these?
```

## Example 3: "What's the queue looking like?"

**User says:** "How's our support queue?"

**Skill routes to:** WORKFLOW 3 (Queue Management)

**Tool calls:**
```
1. get_queue_status()
   → {total_open: 23, urgent: 3, high: 5, avg_wait: "12 min", sla_at_risk: 2}

2. list_agents()
   → [{name: "Agent A", status: "available", load: 3}, {name: "Agent B", status: "available", load: 5}, {name: "Agent C", status: "busy", load: 8}]
```

**Response:**
```
## Queue Status

| Metric | Value | Status |
|--------|-------|--------|
| Open conversations | 23 | ⚠️ Above average |
| Urgent | 3 | 🚨 Needs attention |
| Avg wait time | 12 min | ✅ Within SLA |
| SLA at risk | 2 | ⚠️ Action needed |

### Agent Capacity
| Agent | Status | Load |
|-------|--------|------|
| Agent A | 🟢 Available | 3 conversations |
| Agent B | 🟢 Available | 5 conversations |
| Agent C | 🔴 Busy | 8 conversations |

### Recommendations:
- 2 conversations at SLA risk — assign to Agent A (lowest load)
- 3 urgent conversations need immediate attention
- Agent C is overloaded — consider rebalancing

Want me to assign the at-risk conversations?
```

## Example 4: "Show me our CSAT scores"

**User says:** "How are our satisfaction scores this month?"

**Skill routes to:** WORKFLOW 4 (Service Metrics)

**Tool calls:**
```
1. get_satisfaction_scores()
   → {csat: 4.2, nps: 32, effort_score: 3.8, response_count: 156}

2. get_service_metrics()
   → {avg_response_time: "8 min", first_contact_resolution: 0.72, volume: 340, avg_resolution_time: "2.3 hours"}
```

**Response:**
```
## Service Metrics — This Month

### Satisfaction
| Metric | Score | Trend | Benchmark |
|--------|-------|-------|-----------|
| CSAT | 4.2/5 | ↗️ +0.1 | Good (target: 4.5) |
| NPS | +32 | → Stable | Good (target: +40) |
| Effort Score | 3.8/5 | ↘️ -0.2 | ⚠️ Needs attention |

### Operations
| Metric | Value | Status |
|--------|-------|--------|
| Avg response time | 8 min | ✅ (target: < 15 min) |
| First contact resolution | 72% | ✅ (target: > 70%) |
| Volume | 340 conversations | ↗️ +12% |
| Avg resolution time | 2.3 hours | ✅ (target: < 4h) |

### Insights:
- Effort score declining — customers finding it harder to get help. Investigate KB gaps.
- Volume up 12% — may need additional agent capacity.
- FCR strong at 72% — KB-first approach working.
```
