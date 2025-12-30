---
title: Priority Badges - Visual Demo
description: Generated when testing badging feature. Still needs to be reviewed as of 20251227 for alignment with original MVP plans.
---

# Priority Badges - Visual Demo

This page shows exactly what priority badges look like on your MkDocs site.

You can see an example page [here](../../requirements/requirements-index-example.md).

---

## Individual Requirement Page

When viewing a requirement document, badges appear automatically after the title:

### Example: Plant Database Requirement

<div markdown style="border: 2px solid #e5e7eb; border-radius: 8px; padding: 20px; background-color: #ffffff; margin: 20px 0;">

# Plant Database

<div class="requirement-badges">
    <span class="priority-badge priority-critical">CRITICAL</span>
    <span class="phase-badge">Phase 1</span>
    <span class="status-badge status-approved">Approved</span>
</div>

**Purpose:** Plant data model, storage, and basic display

**Context:** Foundation for entire system - all other features depend on plant data existing.

---

</div>

### Example: Weather Integration Requirement

<div markdown style="border: 2px solid #e5e7eb; border-radius: 8px; padding: 20px; background-color: #ffffff; margin: 20px 0;">

# Weather Integration

<div class="requirement-badges">
    <span class="priority-badge priority-medium">MEDIUM</span>
    <span class="phase-badge">Phase 3</span>
    <span class="status-badge status-in-review">In Review</span>
</div>

**Purpose:** Weather data integration, alerts, and protection planning

**Context:** Protects user plants from weather damage.

---

</div>

### Example: Admin Account Management Requirement

<div markdown style="border: 2px solid #e5e7eb; border-radius: 8px; padding: 20px; background-color: #ffffff; margin: 20px 0;">

# Admin Account Management

<div class="requirement-badges">
    <span class="priority-badge priority-low">LOW</span>
    <span class="phase-badge">Phase 7</span>
    <span class="status-badge status-draft">Draft</span>
</div>

**Purpose:** System admin and community lead account management

**Context:** Highest security risk - currently de-prioritized per REQ-000b.

---

</div>

---

## Requirements Index Page

### Priority Legend

<div class="priority-legend">
    <div class="priority-legend-item">
        <span class="priority-badge priority-critical">CRITICAL</span>
        <span>Foundation features - blocking other work</span>
    </div>
    <div class="priority-legend-item">
        <span class="priority-badge priority-high">HIGH</span>
        <span>Core functionality - needed for MVP</span>
    </div>
    <div class="priority-legend-item">
        <span class="priority-badge priority-medium">MEDIUM</span>
        <span>Important features - can be phased</span>
    </div>
    <div class="priority-legend-item">
        <span class="priority-badge priority-low">LOW</span>
        <span>Nice-to-have - deferred to later</span>
    </div>
</div>

---

### Requirement Cards

<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Plant Database</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-critical">CRITICAL</span>
            <span class="phase-badge">Phase 1</span>
            <span class="status-badge status-approved">Approved</span>
        </div>
    </div>
    <p class="requirement-card-description">
        Plant data model, storage, and basic display. Foundation for entire system - all other features depend on this.
    </p>
    <a href="req-general-user-plant-database.md">View Requirement →</a>
</div>

<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Plant Search</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-critical">CRITICAL</span>
            <span class="phase-badge">Phase 1</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        Search functionality for finding plants by name. Primary discovery mechanism for all users.
    </p>
    <a href="req-general-user-plant-search.md">View Requirement →</a>
</div>

<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Frost Date Calculations</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-high">HIGH</span>
            <span class="phase-badge">Phase 2</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        Calculate frost dates and planting dates based on USDA zone. Critical for location-based planting guidance.
    </p>
    <a href="req-general-user-calculations.md">View Requirement →</a>
</div>

<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Weather Integration</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-medium">MEDIUM</span>
            <span class="phase-badge">Phase 3</span>
            <span class="status-badge status-in-review">In Review</span>
        </div>
    </div>
    <p class="requirement-card-description">
        Weather data integration, alerts, and protection planning. Helps users protect plants from weather damage.
    </p>
    <a href="req-general-user-weather.md">View Requirement →</a>
</div>

<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Admin Account Management</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-low">LOW</span>
            <span class="phase-badge">Phase 7</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        System admin and community lead account management. Highest security risk, currently de-prioritized.
    </p>
    <a href="req-admin-account-management.md">View Requirement →</a>
</div>

---

## Inline Badge Usage

You can also use badges inline in lists:

### By Priority

**Critical Priority Requirements:**

- Plant Database <span class="priority-badge priority-critical">CRITICAL</span>
- Plant Search <span class="priority-badge priority-critical">CRITICAL</span>
- Plant Filter <span class="priority-badge priority-critical">CRITICAL</span>

**High Priority Requirements:**

- Frost Date Calculations <span class="priority-badge priority-high">HIGH</span>
- USDA Zone Integration <span class="priority-badge priority-high">HIGH</span>

**Medium Priority Requirements:**

- Weather Integration <span class="priority-badge priority-medium">MEDIUM</span>
- User Notifications <span class="priority-badge priority-medium">MEDIUM</span>
- General Resources <span class="priority-badge priority-medium">MEDIUM</span>

**Low Priority Requirements:**

- Admin Account Management <span class="priority-badge priority-low">LOW</span>
- Educator Role <span class="priority-badge priority-low">LOW</span>
- Elevated Access <span class="priority-badge priority-low">LOW</span>

---

## Mobile View

Badges adapt to smaller screens:

<div markdown style="max-width: 375px; border: 2px solid #e5e7eb; padding: 10px; margin: 20px 0;">

### Plant Database

<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.5rem 0;">
    <span class="priority-badge priority-critical" style="font-size: 0.75rem; padding: 0.2rem 0.5rem;">CRITICAL</span>
    <span class="phase-badge" style="font-size: 0.75rem; padding: 0.2rem 0.5rem;">Phase 1</span>
</div>

Plant data model and storage...

</div>

---

## Dark Mode

Badges automatically adapt to dark mode:

<div markdown style="background-color: #1e293b; color: #f1f5f9; border: 2px solid #334155; border-radius: 8px; padding: 20px; margin: 20px 0;">

# Plant Database

<div class="requirement-badges">
    <span class="priority-badge priority-critical">CRITICAL</span>
    <span class="phase-badge">Phase 1</span>
    <span class="status-badge status-approved">Approved</span>
</div>

**Purpose:** Plant data model, storage, and basic display

**Context:** Foundation for entire system

---

</div>

---

## ASCII Preview (No CSS)

If you can't render the HTML above, here's what the badges look like in plain text:


<div class="ascii-art">

```
┌─────────────────────────────────────────────────────────────────┐
│ Plant Database                                                  │
│ [  CRITICAL  ] [ Phase 1 ] [ Approved ]                         │
│                                                                 │
│ Purpose: Plant data model, storage, and basic display           │
│ Context: Foundation for entire system                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Weather Integration                                             │
│ [  MEDIUM  ] [ Phase 3 ] [ In Review ]                          │
│                                                                 │
│ Purpose: Weather data integration and alerts                    │
│ Context: Protects user plants from weather damage               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Admin Account Management                                        │
│ [   LOW   ] [ Phase 7 ] [ Draft ]                               │
│                                                                 │
│ Purpose: System admin and community lead management             │
│ Context: Highest security risk - currently de-prioritized       │
└─────────────────────────────────────────────────────────────────┘
```
</div>

---

## Color Reference

### Priority Colors

| Badge | Background | Border | Text | Use Case |
|-------|------------|--------|------|----------|
| <span class="priority-badge priority-critical">CRITICAL</span> | `#ef4444` (Red) | `#dc2626` (Dark Red) | White | Foundation, blocking |
| <span class="priority-badge priority-high">HIGH</span> | `#f97316` (Orange) | `#ea580c` (Dark Orange) | White | Core MVP features |
| <span class="priority-badge priority-medium">MEDIUM</span> | `#eab308` (Yellow) | `#ca8a04` (Gold) | Dark | Important, phased |
| <span class="priority-badge priority-low">LOW</span> | `#22c55e` (Green) | `#16a34a` (Dark Green) | White | Deferred, nice-to-have |

### Status Colors

| Badge | Background | Border | Text |
|-------|------------|--------|------|
| <span class="status-badge status-draft">Draft</span> | `#9ca3af` (Gray) | `#6b7280` | White |
| <span class="status-badge status-in-review">In Review</span> | `#3b82f6` (Blue) | `#2563eb` | White |
| <span class="status-badge status-approved">Approved</span> | `#10b981` (Green) | `#059669` | White |
| <span class="status-badge status-implemented">Implemented</span> | `#8b5cf6` (Purple) | `#7c3aed` | White |

---

## Testing Your Badges

To see these badges live on your site:

1. **Start MkDocs:**

   ```bash
   mkdocs serve
   ```

2. **Visit this page:**

   ```
   http://localhost:8000/tutorials/mkdocs/priority-badges-visual-demo/
   ```

3. **Create a test requirement:**

   - Copy `docs/templates/requirements-template.md`
   - Save as `docs/requirements/req-test-example.md`
   - Fill in the YAML front matter
   - View at `http://localhost:8000/requirements/req-test-example/`

---

**Next:** See [Priority Badges Setup Guide](priority-badges-setup.md) for configuration details.
