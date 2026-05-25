#!/usr/bin/env python3
"""
Customer Churn Risk Scorer
Calculates composite churn risk from multiple signals.
Usage: python churn_score.py '{"health": 30, "tickets_30d": 3, "sentiment": "declining", "plan": "pro", "tenure_months": 18}'
"""
import json
import sys

SIGNAL_WEIGHTS = {
    "low_health": 25,          # health < 50
    "critical_health": 15,     # health < 30 (additional)
    "high_ticket_volume": 20,  # 3+ tickets in 30 days
    "negative_sentiment": 15,  # declining or negative
    "billing_complaint": 10,   # recent billing issue
    "declining_usage": 15,     # usage dropping
    "short_tenure": 5,         # < 6 months
    "no_recent_login": 10,     # no login in 14+ days
}

def calculate_churn_score(data: dict) -> dict:
    score = 0
    signals = []
    actions = []

    health = data.get("health", 100)
    tickets_30d = data.get("tickets_30d", 0)
    sentiment = data.get("sentiment", "stable")
    plan = data.get("plan", "free")
    tenure = data.get("tenure_months", 12)
    has_billing_complaint = data.get("billing_complaint", False)
    usage_trend = data.get("usage_trend", "stable")
    days_since_login = data.get("days_since_login", 0)

    if health < 50:
        score += SIGNAL_WEIGHTS["low_health"]
        signals.append("Health score below 50")
    if health < 30:
        score += SIGNAL_WEIGHTS["critical_health"]
        signals.append("Critical health (below 30)")
        actions.append("Immediate intervention required")

    if tickets_30d >= 3:
        score += SIGNAL_WEIGHTS["high_ticket_volume"]
        signals.append(f"{tickets_30d} support tickets in 30 days")
        actions.append("Review ticket themes for systemic issues")

    if sentiment in ("declining", "negative"):
        score += SIGNAL_WEIGHTS["negative_sentiment"]
        signals.append(f"Sentiment: {sentiment}")

    if has_billing_complaint:
        score += SIGNAL_WEIGHTS["billing_complaint"]
        signals.append("Recent billing complaint")
        actions.append("Prioritize billing resolution")

    if usage_trend == "declining":
        score += SIGNAL_WEIGHTS["declining_usage"]
        signals.append("Usage declining")
        actions.append("Send re-engagement content")

    if tenure < 6:
        score += SIGNAL_WEIGHTS["short_tenure"]
        signals.append("Short tenure (< 6 months)")

    if days_since_login > 14:
        score += SIGNAL_WEIGHTS["no_recent_login"]
        signals.append(f"No login in {days_since_login} days")
        actions.append("Proactive outreach recommended")

    # Cap at 100
    score = min(score, 100)

    # Risk level
    if score >= 70: risk = "high"
    elif score >= 40: risk = "medium"
    else: risk = "low"

    # Plan-based urgency
    urgency = "normal"
    if plan == "enterprise" and score >= 40:
        urgency = "critical"
        actions.insert(0, "CRITICAL: Enterprise customer at risk — executive escalation")
    elif plan == "pro" and score >= 60:
        urgency = "high"
        actions.insert(0, "HIGH: Pro customer at risk — retention team outreach")

    return {
        "score": score,
        "risk": risk,
        "urgency": urgency,
        "signals": signals,
        "recommended_actions": actions,
        "plan": plan,
        "health": health,
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python churn_score.py \'{"health": 30, "tickets_30d": 3, "sentiment": "declining"}\'')
        sys.exit(1)
    data = json.loads(sys.argv[1])
    print(json.dumps(calculate_churn_score(data), indent=2))
