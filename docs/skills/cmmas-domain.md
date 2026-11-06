# CMMS Domain Skill

Core concepts for the CMMS project. Keep short and practical.

## Core Entities
- **Asset (Equipment)**: asset_id, name, category, make, model, serial, vendor, purchase_date, warranty_expiry, location, status, risk_class
- **PPM Work Order**: generated from schedule; checklist template; technician notes/photos; sign-off
- **Breakdown**: reported by, urgency, assigned engineer, diagnosis, action, parts, cost, vendor, downtime, rectification time, status
- **Document**: service reports, calibration certs, warranty, AMC, manuals; linked to asset; expiry alerts
- **User/Role**: admin-editable roles; audit log

## Key Metrics
- PPM compliance %
- MTTR (mean time to repair)
- Downtime per equipment
- Repeat failures per device
- Response time, repair time, downtime

## Domain Language
- In-house engineer vs external vendor
- AMC (Annual Maintenance Contract)
- Calibration certificate expiry
- SHCC audit pack: register, PPM chart, certs file, breakdown register — all "to be verified against official checklist".

## Keep Updated
- Add terms as they arise in the build.
