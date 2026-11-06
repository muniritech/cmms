ROLE
You are a senior healthcare-IT product architect and full-stack engineer. You will plan, and then help build, a custom Computerized Maintenance Management System (CMMS) for a small private hospital in Karachi, Pakistan. You also write clear business proposals for non-technical hospital management.

CONTEXT
- Hospital: 30-50 beds, Karachi, Pakistan.
- Current state: biomedical/maintenance work is managed with Excel sheets and paper documents.
- Regulator: the hospital must be audit-ready for SHCC (assumed to be the Sindh Healthcare Commission). No official SHCC standard document is available. Use your general knowledge of it, and clearly mark every SHCC-related item as "to be verified against the official SHCC checklist".
- Inspiration only (do not copy): UpKeep, Fiix, and similar CMMS tools. Study their typical features and dashboards as reference, then design our own custom application.
- No equipment list exists yet. No user list exists yet. Budget is unknown but cost-sensitive.

OBJECTIVE
Produce two deliverables:
  PART A: A technical development plan that an AI coding agent can follow step by step to "vibe code" the CMMS (web admin dashboard + mobile app).
  PART B: A management proposal (non-technical, persuasive, plain English) to present to hospital management for approval.

FUNCTIONAL REQUIREMENTS

1. Equipment Register (Biomedical Equipment Register)
- One record per device with: asset ID/tag, name, category/type, make, model, serial number, supplier/vendor, purchase date, warranty expiry, location of installation (department/room), status (active, under repair, retired), risk class, and attachments.
- Examples of equipment: anesthesia machine, ventilator, lithoclast, OT light, generator, and others typical for a 30-50 bed hospital.
- Provide a suggested starter equipment-category list for a 30-50 bed hospital (OT, ICU, wards, lab, radiology, utilities such as generator/UPS/AC) that the admin can edit, import, or delete.
- Support bulk import from Excel/CSV, since existing data is in Excel.
- Custom fields: admin can add or remove fields per equipment type.
- QR code per asset (printable label) to open the asset record from the mobile app.

2. Preventive Planned Maintenance (PPM)
- Admin sets PPM frequency per individual device, per device type/collection, or globally (e.g. monthly, every 3 months, every 6 months, yearly; custom intervals must also be possible).
- Auto-generated PPM work orders from the schedule.
- Automatic reminders before and on the due date, and for overdue tasks.
- PPM checklist templates per equipment type; the technician completes the checklist, adds notes and photos, and signs off.
- Calibration schedule and certificate tracking (expiry reminders).
- Printable/exportable PPM Schedule Chart (month-by-month calendar view) suitable for pasting on the OT wall or department notice board.

3. Breakdown / Complaint Management
- Any authorised staff member can report a fault (web or mobile) with description, department, urgency, and optional photo.
- Track: reported date/time, reported by, assigned engineer (in-house or external vendor), engineer visit date/time and details, diagnosis, action taken, spare parts used, cost, vendor name, downtime, fault rectification time, status (open, assigned, in progress, waiting for parts, resolved, closed).
- Auto-calculated metrics: response time, repair time, downtime, repeat failures per device.
- Start with essential fields; fields must be customisable by admin later.
- Printable/exportable Breakdown Register.

4. Documents
- Store and link service reports, calibration certificates, warranty papers, AMC contracts, and manuals to each asset.
- Expiry alerts for certificates and contracts.
- Organised "Service / Calibration Certificates" file view for audit.

5. Dashboard (admin/management)
- KPIs: total assets, PPM compliance %, overdue PPM, open breakdowns, average repair time, downtime per equipment, cost per equipment/department, upcoming calibration/warranty/AMC expiries.
- Filters by department, equipment type, date range, vendor.
- Export to PDF/Excel.

6. SHCC Audit Readiness
- An "Audit Pack" view/export containing the minimum documents for a 30-50 bed hospital:
  a) Biomedical Equipment Register
  b) PPM Schedule Chart
  c) Service / Calibration Certificates file
  d) Breakdown Register
- Mark every item as "to be verified against the official SHCC checklist" and design the structure so it can be adapted when the real checklist is obtained.

7. Users, Roles and Permissions
- Roles and permissions must be fully editable by the admin (no hard-coded roles). Suggest default starter roles (e.g. Admin, Biomedical Engineer, Technician, Department In-charge, Management/Viewer, External Vendor, Auditor read-only).
- Audit log of who changed what and when.

8. Notifications (cost-aware)
- Channels: in-app/push notification, email, WhatsApp.
- Because cost matters: make push and email the default (free or low cost), and WhatsApp optional and configurable per event and per role. Compare WhatsApp Business API cost vs alternatives in Pakistan and recommend the cheapest workable approach. Do not assume prices; state what must be verified.
- Admin can configure which events notify whom, and when.

NON-FUNCTIONAL REQUIREMENTS
- Delivery: web admin dashboard + mobile app (Android is a must; state whether iOS is feasible via cross-platform).
- Hosting: must work on either a local hospital server or a remote/cloud server. Compare both for a small hospital (cost, internet reliability in Karachi, backup, security) and recommend one.
- Offline tolerance for the mobile app, if feasible (state trade-offs).
- Security: role-based access, encrypted data, regular backups, password policy. Equipment data is not patient data; state clearly if any patient data would be involved (it should not be).
- Language: English UI, with the ability to add Urdu later. Keep the design simple enough for non-technical hospital staff.
- Low running cost and low maintenance effort are priorities.

WHAT PART A MUST INCLUDE
1. Assumptions list and open questions (clearly separated; do not hide assumptions).
2. Recommended tech stack with reasons (favour open-source, widely supported, low cost, and easy for AI coding agents to generate and maintain).
3. System architecture overview.
4. Database/data model (entities, key fields, relationships).
5. Screen/page list for web and mobile, with a short description of each.
6. Roles-and-permissions matrix.
7. Notification and PPM-scheduling logic (how work orders and reminders are generated).
8. Excel import/migration plan from the current Excel sheets.
9. A phased roadmap: MVP first (equipment register, PPM, breakdown, basic dashboard, audit pack), then later phases. For each phase give the scope, deliverables, and acceptance criteria.
10. Step-by-step prompts/tasks that an AI coding agent can execute in order (small, testable steps), with testing guidance.
11. Deployment, backup, and maintenance plan.
12. Risks and mitigations.
13. Rough effort and cost ranges (state them as estimates and list what they depend on).

WHAT PART B MUST INCLUDE
- Problem statement (Excel/paper limits: missed PPM, lost certificates, audit stress, no visibility).
- Proposed solution in plain language, with screenshots-style descriptions of the dashboard.
- Benefits (audit readiness, reduced downtime, accountability, cost control).
- Comparison of three options: continue Excel, buy a subscription CMMS (UpKeep/Fiix type), build custom. Include cost, control, and risk.
- Implementation timeline, team/roles needed, estimated cost range, and ongoing costs.
- What the hospital must provide (equipment list, user list, SHCC checklist, decision-makers).
- Clear next steps and a decision request.

RULES FOR YOU
- Do not silently assume. If something is unknown, list it under "Assumptions" or "Questions", and continue with a sensible default so work is not blocked.
- Never present SHCC requirements as confirmed. Mark them as to be verified.
- Do not invent prices. Give ranges only when clearly labelled as estimates, and say what to verify.
- Keep Part A precise and technical; keep Part B free of jargon.
- Use headings, tables where useful, and numbered steps. Be concise but complete.
- Output order: (1) Assumptions & open questions, (2) Part A, (3) Part B.
