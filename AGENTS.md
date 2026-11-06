# AGENTS.md — CMMS Project (Source of Truth)

## Project Goal
Build a custom CMMS for a small private hospital (30–50 beds, Karachi) with:
- Web admin dashboard
- Mobile app (PWA first; native Android later)
- Deliverables: technical build plan (Part A) + management proposal (Part B)

## Tech Stack Decisions (proposed, pending approval)
- Backend: Python FastAPI
- Database: SQLite (MVP) → PostgreSQL (later)
- Web: React + Vite + Tailwind + Recharts
- Mobile: PWA (React) → native Android (later)
- Auth: JWT + RBAC
- Exports: PDF + Excel
- QR codes: standard generator

## Coding Conventions
- Small, testable steps. One concern per change.
- All new/changed endpoints return JSON with consistent error shape.
- Use environment variables for secrets; `.env.example` file.

## Folder Map
```
backend/    - FastAPI app, models, schemas, routes, scheduler
web/        - React admin dashboard
mobile/     - PWA app
scripts/    - Utility scripts (exports, imports)
tests/      - Test suite
docs/       - Plans, skills, proposals
```

## How to Run and Test
- Backend: `uvicorn main:app --reload` (once scaffolded)
- Web: `vite dev` (once scaffolded)
- Mobile: `npm start` / build (once scaffolded)

## Definition of Done
- Working feature end-to-end
- Unit/integration tests pass
- Documentation updated

## Rules from Brief
- Plan, act, verify, log.
- Small tasks.
- Update PROJECT_LOG.md at end of session.
- No destructive commands without asking.
- Never hard-code secrets.
- Mark SHCC items as "to be verified".
- No invented prices/regulations.
- Commit small meaningful changes.
