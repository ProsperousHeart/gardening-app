---
title: Requirements Index Example
description: Example of how the priority badges coud be used throughout the site.
---
# Requirements Index

This page demonstrates how priority badges appear in the MkDocs site.

## Priority Legend

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

## Phase 1: Core Plant Database

### Plant Database
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

### Plant Search
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

### Plant Filter
<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">Plant Filter</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-critical">CRITICAL</span>
            <span class="phase-badge">Phase 1</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        Advanced filtering by plant characteristics, zones, and timing. Helps users find plants matching specific criteria.
    </p>
    <a href="req-general-user-plant-filter.md">View Requirement →</a>
</div>

---

## Phase 2: Supporting Calculations & Data

### Calculations
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

### USDA Zones
<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">USDA Zone Integration</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-high">HIGH</span>
            <span class="phase-badge">Phase 2</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        USDA hardiness zone data and location mapping. Foundation for all location-based features.
    </p>
    <a href="req-general-user-usda-zones.md">View Requirement →</a>
</div>

---

## Phase 3: User Experience Enhancements

### Weather Integration
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

### Notifications
<div class="requirement-card">
    <div class="requirement-card-header">
        <h4 class="requirement-card-title">User Notifications</h4>
        <div class="requirement-card-meta">
            <span class="priority-badge priority-medium">MEDIUM</span>
            <span class="phase-badge">Phase 3</span>
            <span class="status-badge status-draft">Draft</span>
        </div>
    </div>
    <p class="requirement-card-description">
        User notification preferences and delivery. Keeps users informed of weather, system updates, and community events.
    </p>
    <a href="req-general-user-notifications.md">View Requirement →</a>
</div>

---

## Phase 7: Admin Features (Deferred)

### Account Management
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

## Filter by Priority

### Critical Priority (3)
- [Plant Database](req-general-user-plant-database.md) <span class="priority-badge priority-critical">CRITICAL</span>
- [Plant Search](req-general-user-plant-search.md) <span class="priority-badge priority-critical">CRITICAL</span>
- [Plant Filter](req-general-user-plant-filter.md) <span class="priority-badge priority-critical">CRITICAL</span>

### High Priority (2)
- [Calculations](req-general-user-calculations.md) <span class="priority-badge priority-high">HIGH</span>
- [USDA Zones](req-general-user-usda-zones.md) <span class="priority-badge priority-high">HIGH</span>

### Medium Priority (2)
- [Weather](req-general-user-weather.md) <span class="priority-badge priority-medium">MEDIUM</span>
- [Notifications](req-general-user-notifications.md) <span class="priority-badge priority-medium">MEDIUM</span>

### Low Priority (1)
- [Account Management](req-admin-account-management.md) <span class="priority-badge priority-low">LOW</span>

---

## Quick Stats

| Priority | Count | Percentage |
|----------|-------|------------|
| CRITICAL | 3     | 37.5%      |
| HIGH     | 2     | 25.0%      |
| MEDIUM   | 2     | 25.0%      |
| LOW      | 1     | 12.5%      |
| **Total** | **8** | **100%**   |

---

*This is an example page showing how priority badges would appear. In production, this page could be auto-generated from the requirement files.*
