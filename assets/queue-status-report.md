# Queue Status Report Template

---

## Support Queue — {timestamp}

### Summary
| Metric | Value | Status |
|--------|-------|--------|
| Open conversations | {total_open} | {status_emoji} |
| Urgent | {urgent_count} | {status_emoji} |
| High priority | {high_count} | {status_emoji} |
| Avg wait time | {avg_wait} | {status_emoji} |
| SLA at risk | {sla_at_risk} | {status_emoji} |

### Agent Capacity
| Agent | Status | Load | Available |
|-------|--------|------|-----------|
| {agent_name} | {status_emoji} {status} | {load} conversations | {available_capacity} |

### SLA At-Risk Conversations
| Conv ID | Customer | Wait Time | SLA Remaining | Priority |
|---------|----------|-----------|---------------|----------|
| {id} | {customer_name} | {wait_time} | ⚠️ {remaining} | {priority} |

### Recommendations
1. {specific_action_1}
2. {specific_action_2}
3. {specific_action_3}

---

*Generated from mcp-customer-service | {timestamp}*
