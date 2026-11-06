# RBAC Design Skill

Editable role-based access control design.

## Roles (starter; editable by admin)
- Admin (full permissions)
- Biomedical Engineer (create/read/update PPM, breakdowns)
- Technician (complete checklists, log breakdowns, upload photos)
- Department In-charge (view assets, approve work orders)
- Management/Viewer (view KPIs, dashboards, audit pack)
- External Vendor (log vendor work, report parts, cost)
- Auditor (read-only; access audit pack)

## Permissions (example)
- Create/read/update/delete assets: Admin only
- Edit PPM schedule: Admin
- Complete PPM: Technician
- Report breakdown: Any authorized (staff, vendor)
- View audit pack: Auditor, Management
- Configure roles/fields: Admin only

## Audit Log
- Capture who changed what, when
- Keep immutable log of user actions

## Implementation Notes
- Permissions are stored in DB; roles map to permissions.
- Roles can be added/removed by admin via web UI.
