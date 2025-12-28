---
title: Priority-Based Implementation Order
description: GenAI suggested order of MVP items in phases. Still needs to be reviewed as of 20251227 for alignment with original MVP plans. It also seems to be for more than just an MVP.
---

## [Priority-Based Implementation Order](./MVP_PRI_Based_Order.md)

Based on **REQ-000b_Scope.md** performance criteria and business value:

### Phase 1: Core Plant Database

**Priority**: CRITICAL - Foundation for entire system

1. `req-general-user-plant-database.md`
2. `req-general-user-plant-search.md`
3. `req-general-user-plant-filter.md`

**Why First:**
- All other features depend on plant data existing
- Provides immediate value to users
- Simplest to implement (no authentication/authorization complexity)
- Can be used to validate development workflow

**Performance Criteria:**
- View plant data (common name, scientific name, germination info, etc.)
- Search for plants by name
- Filter by characteristics or timing based on USDA zone
- based on performance criteria for the [plant database](../../requirements/REQ-000b_Scope.md#starting-deliverable--plant-database), [views & filters](../../requirements/REQ-000b_Scope.md#starting-deliverable--decision-on-views--filters) with consideration of plans for a [pest database](../../requirements/REQ-000b_Scope.md#starting-deliverable--pest-database)

### Phase 2: Supporting Calculations & Data

**Priority**: HIGH - Enables core use cases

4. `req-general-user-calculations.md`
5. `req-general-user-usda-zones.md`

**Why Second:**
- Required for plant recommendations
- Frost date calculations enable planting planning
- USDA zone filtering critical for location-based features

**Performance Criteria:**
- Calculate first/last frost dates from USDA zone
- Calculate planting dates based on plant requirements
- Provide date-based recommendations
- based on [performance criteria](../../requirements/REQ-000b_Scope.md#starting-deliverable--calculations)

### Phase 3: User Experience Enhancements

**Priority**: HIGH - Improves usability and retention

6. `req-general-user-weather.md`
7. `req-general-user-notifications.md`
8. `req-general-user-general-resources.md`

**Why Third:**
- Weather integration provides protection alerts
- Notifications improve engagement
- Resources help users succeed with gardening

**Performance Criteria:**
- Connect to weather API
- Provide protection warnings
- Display gardening resources
- weather should follow [this](../../requirements/REQ-000b_Scope.md#weather) performance criteria

### Phase 4: User Data & Feedback

**Priority**: MEDIUM - Enables personalization

9. `req-general-user-feedback.md`
10. `req-general-user-account-favorites.md`
11. `req-general-user-add-plant.md`

**Why Fourth:**
- Feedback loop for continuous improvement
- Favorites enable personalization
- User-contributed plants expand database

**Performance Criteria:**
- Submit feedback and bug reports - [feedback](../../requirements/REQ-000b_Scope.md#user-feedback)
- Save favorite plants locally/cloud - [account favorites](../../requirements/REQ-000b_Scope.md#account-favorites)
- Request new plants for database - [add plant](../../requirements/REQ-000b_Scope.md#add-plant)

### Phase 5: Advanced General Features

**Priority**: MEDIUM - Nice-to-have enhancements

12. `req-general-user-moon-gardening.md`
13. `req-general-user-pest-database.md`

**Why Fifth:**
- Moon gardening is specialized feature
- Pest database extends plant care
- Not critical for MVP

**Performance Criteria:**
- Calculate moon phases - [moon gardening](../../requirements/REQ-000b_Scope.md#moon-based-gardening)
- Provide moon-based planting suggestions
- Track common pests and organic treatments - [pest database](../../requirements/REQ-000b_Scope.md#starting-deliverable--pest-database)

### Phase 6: Community Features

**Priority**: MEDIUM - Secondary user segment

14. `req-community-member-announcements.md`
15. `req-community-member-plot-management.md`
16. `req-community-member-team-chores.md`
17. `req-community-member-apprentice-program.md`

**Why Sixth:**

- Depends on user authentication being implemented
- Serves smaller user segment (community gardens)
- More complex security requirements

**Performance Criteria:**

- Secure community-specific access - [community member](../../requirements/REQ-000b_Scope.md#primary-deliverable--general-community-member-access)
- Plot tracking and assignment - [plot assignment](../../requirements/REQ-000b_Scope.md#plot-assignment-system)
- Team/chore coordination - [team & chores](../../requirements/REQ-000b_Scope.md#team--chores)
- Training program tracking - [apprentice program](../../requirements/REQ-000b_Scope.md#apprentice-program)

### Phase 7: Admin Features

**Priority**: LOW - Currently de-prioritized

18. `req-admin-account-management.md`
19. `req-admin-educator-role.md`
20. `req-admin-elevated-access.md`

**Why Last:**

- Highest security risk
- Serves smallest user segment
- Can be handled manually initially

**Performance Criteria:**

- Create/manage community leads - [account management](../../requirements/REQ-000b_Scope.md#starting-deliverable--account-management)
- Assign roles and permissions
- View/manage all accounts - [elevated view access](../../requirements/REQ-000b_Scope.md#starting-deliverable--elevated-view-access)