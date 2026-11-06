# PPM Scheduling Skill

Rules for generating recurring maintenance work orders.

## Frequencies
- Monthly, every 3 months, every 6 months, yearly
- Custom intervals (days) allowed, set per asset, per type, or globally

## Generation Logic
- Scheduler runs periodically (e.g., daily at 00:05)
- For each active asset with PPM: compute next due date from last completed (or last performed) date + interval
- If next due date <= today + reminder window (e.g., 7 days): generate reminder notifications; if past due: generate overdue alerts

## Reminders
- Before due: N days (default 7)
- On due: alert
- Overdue: escalation alerts

## Checklist Templates
- Per equipment type
- Technician completes checklist, adds notes + photos, signs off
