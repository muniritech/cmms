# ASSUMPTIONS — CMMS Project

These are the defaults proposed where IDEA.md was silent. Each is clearly a **proposal**, not a fact.

## Resolved from user answers (2026-11-06)
1. **Hosting**: Local server preferred for now → cloud VPS fallback to be evaluated later. (Assumption confirmed by user.)
2. **Mobile delivery**: PWA acceptable for now → native Android build planned for Phase 2+ if PWA proves insufficient. (Assumption confirmed by user.)
3. **User count**: ~20 users total. (Assumption from user estimate.)

## Proposed Defaults (pending approval)

### Tech stack (proposed)
- Backend: Python FastAPI + SQLite (MVP) / PostgreSQL (later)
- Web admin: React + Vite + Tailwind + Recharts
- Mobile: PWA (React) → native Android (Kotlin/Flutter) later
- Auth: JWT + RBAC
- Scheduler: APScheduler (backend) or background jobs
- Exports: PDF via ReportLab/weasyprint, Excel via openpyxl/pandas
- QR: qrcode/pyqrcode or QRCode.js

### Notifications (proposed defaults)
- Push: Web Push / Firebase (free tier) → default
- Email: SMTP (low cost) → default
- WhatsApp: Twilio/FastAPI WhatsBridge → optional, per-event/per-role configurable (cost to be verified)

### PPM defaults (proposed)
- Intervals: monthly, 3, 6, 12 months; custom via admin
- Reminders: 7 days before + on due date + overdue escalations

### Starter equipment categories (proposed)
- OT, ICU, General Ward, Pediatrics, Surgical (OT), Lab, Radiology, Pharmacy, Engineering/Utilities (generator, UPS, AC, boiler), Kitchen, ER

### SHCC
- All SHCC-related items marked "to be verified against the official SHCC checklist".

## Open Questions
- None blocking — user provided answers to the 5 essential questions.
