# Customer Service Cross-MCP Workflows

## CS + CRM: Full Customer Context

### Before responding → Enrich with CRM data
```
CS: get_customer_profile(id: "cust-456") → {plan: "Enterprise", health: 45}
CRM: search_contacts(query: "cust-456") → {name: "Sarah", deals: [{name: "Renewal", value: 120000, stage: "Negotiation"}]}
CS: add_internal_note(id: "conv-123", body: "⚠️ CRM: Active $120k renewal in Negotiation. Handle with extreme care. Contact: Sarah Mitchell, VP Eng.")
```

### After resolution → Update CRM activity
```
CS: resolve_conversation(id: "conv-123", summary: "Resolved billing discrepancy")
CRM: create_activity(type: "note", subject: "Support ticket resolved: billing discrepancy", record_id: "contact_sarah")
```

## CS + Slack: Team Escalation

### Enterprise customer escalation
```
CS: get_customer_profile(id: "cust-456") → {plan: "Enterprise", health: 45}
CS: escalate(id: "conv-123", reason: "Production outage, Enterprise customer")
SLACK: slack_send_message(
  channel: "#cs-escalations",
  text: "🚨 *Enterprise Escalation*\n*Customer:* Sarah Mitchell (health: 45, declining)\n*Issue:* Production outage\n*Active deal:* $120k renewal in Negotiation\n*Conv:* conv-123\n@cs-lead please review immediately"
)
```

### High churn risk detected
```
CS: assess_churn_risk(id: "cust-789") → {risk: "high", score: 85}
SLACK: slack_send_message(
  channel: "#retention",
  text: "⚠️ *Churn Alert*\nCustomer: James Park (Pro plan, $200/mo)\nRisk score: 85/100\nSignals: declining usage, 3 tickets this month, negative sentiment\nRecommend: Proactive outreach within 24h"
)
```

## CS + Email: Proactive Outreach

### Churn prevention outreach
```
CS: assess_churn_risk(id: "cust-789") → {risk: "high"}
CS: get_customer_profile(id: "cust-789") → {name: "James", email: "james@company.com"}
EMAIL: email_send(
  to: "james@company.com",
  subject: "James — quick check-in from our team",
  body: "Hi James, I noticed you've had a few support interactions recently. I wanted to personally check in and see if there's anything we can do to improve your experience..."
)
CS: start_conversation(customer_id: "cust-789", subject: "Proactive retention outreach", channel: "email")
```

## CS + Notifications: Real-time Alerts

### SLA breach imminent
```
CS: get_queue_status() → {sla_at_risk: [{id: "conv-456", remaining: "5 min"}]}
NOTIFICATIONS: notification_send(
  recipient: assigned_agent_id,
  channel: "push",
  title: "⚠️ SLA breach in 5 min",
  body: "conv-456: Customer waiting 55 min (SLA: 60 min). Respond now.",
  priority: "critical"
)
```

## Full Orchestration: VIP Issue Resolution

```
Step 1 (CS): list_conversations(status: "open", priority: "urgent") → conv-123
Step 2 (CS): get_conversation(id: "conv-123") → full thread
Step 3 (CS): get_customer_profile(customer_id) → Enterprise, health 45
Step 4 (CRM): search_contacts(query: email) → Active $120k deal
Step 5 (CS): assess_churn_risk(customer_id) → HIGH
Step 6 (CS): search_knowledge_base(query: "issue keywords") → KB match
Step 7 (CS): suggest_response(id: "conv-123") → draft
Step 8 (CS): reply_conversation(id: "conv-123", body: personalized_response)
Step 9 (CS): add_internal_note(body: "VIP handling. Churn risk high. Active deal context.")
Step 10 (SLACK): slack_send_message(channel: "#vip-support", text: "Handled VIP conv-123. Churn risk flagged.")
```
