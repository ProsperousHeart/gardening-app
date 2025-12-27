# MVP Specification-Driven Development (SDD) Planning Document

**Purpose**: Plan the generation of detailed requirements files that will feed into specification creation

**Template Source**: `docs/templates/requirements-template.md`

**Security Framework**: CodeGuard (plugin: `codeguard-security@project-codeguard`)

---

## Table of Contents

- [Overview](#overview)
- [Current State Analysis](#current-state-analysis)
- [Requirements Generation Strategy](#requirements-generation-strategy)
- [Priority-Based Implementation Order](#priority-based-implementation-order)
- [Requirements Files to Generate](#requirements-files-to-generate)
- [Agents and Prompts to Use](#agents-and-prompts-to-use)
- [CodeGuard Integration](#codeguard-integration)
- [Workflow Execution Plan](#workflow-execution-plan)
- [Success Criteria](#success-criteria)
- [Next Steps](#next-steps)

---

## Overview

This planning document outlines the systematic approach to creating detailed requirements files for the Gardening Application. These requirements will follow the template at `docs/templates/requirements-template.md` and serve as inputs for specification generation using the established SDD workflow:

```
Requirements → Specifications → Architecture Diagrams → Threat Models → TDD Implementation
```

### Key Principles

1. **Specification-Driven**: All code will be generated from formal specifications
2. **Security-First**: CodeGuard rules integrated from the start
3. **Incremental Delivery**: Components built in priority order based on value and dependencies
4. **Systems Design Methodology**: Formal requirements analysis following Cornell's approach
5. **Traceability**: Complete tracking from requirements → specs → code → tests

---

## Current State Analysis

### Existing [Requirements](../../requirements/README.md) Documentation (REQ-000 Series)

These files contain high-level systems design artifacts (status is estimated and may be flexible depending on stage of completion):

| File | Content | Purpose | Status |
|------|---------|---------|--------|
| `REQ-000a_General.md` | Project description, stakeholders, context | System overview | Complete |
| `REQ-000b_Scope.md` | Context diagrams, scenarios, scope trees | System boundaries | Complete |
| `REQ-000c_UseCases.md` | Actor-based use case table (23+ scenarios) | User interactions | Complete |
| `REQ-000d_UCBDs.md` | Use Case Behavior Diagrams | Behavioral flows | Complete |
| `REQ-000e_Requirements.md` | Centralized requirements table | Requirement specs | Started |
| `REQ-000f_FBDs.md` | Functional Flow Block Diagrams | Functional architecture | Complete |
| `REQ-000g_Decisions.md` | Decision diagrams | Design decisions | Complete |

**Key Finding**: The REQ-000 series provides excellent high-level systems design but lacks the **detailed, implementable requirements** needed to generate specifications following `requirements-template.md`.

### Gap Analysis

**What We Have:**

- System context and boundaries (REQ-000a, REQ-000b)
- High-level scope trees (REQ-000b)
- User roles and scenarios (REQ-000c)
- Behavioral flows (REQ-000d)

**What We Need:**

- **Detailed requirements files** for each component/module/feature following the template structure:

  - Context (purpose, role, users, scenarios)
  - Functional requirements (core features, business logic, state management)
  - UI/UX requirements (layout, visual design, responsive behavior, accessibility)
  - Data requirements (models, schemas, validation, API specs)
  - Integration requirements (dependencies, data flow, external services)
  - Constraints (technical stack, performance, security, design standards)
  - Success criteria (validation checklists)

### System Architecture Summary

Based on **REQ-000b_Scope.md**, the system has three primary deliverables:

1. **GeneralUser** (highest priority) - Core plant database and gardening tools
2. **CommunityMember** (medium priority) - Community garden collaboration (which requires ability to create roles and elevate community garden privileges)
3. **AdminAccess** (lowest priority, currently de-prioritized) - System administration

---

## Requirements Generation Strategy

### Approach

1. **Top-Down Decomposition**: Break down each scope tree deliverable into detailed requirements
2. **Template-Driven**: All requirements files follow `docs/templates/requirements-template.md`
3. **Priority-Based**: Generate requirements in order of business value and technical dependencies
4. **Security-Embedded**: Include CodeGuard security requirements from the start
5. **Traceability**: Link each detailed requirement back to REQ-000 series

### Naming Convention

Requirements files will follow kebab-case naming:

```
docs/requirements/req-{priority}-{subsystem}-{component}.md
```

Examples:

- `req-01-general-user-plant-database.md`
- `req-02-general-user-weather.md`
- `req-10-community-member-announcements.md`
- `req-20-admin-account-management.md`

**Priority prefixes:**

- `01-09`: GeneralUser.ViewsAndInsights (highest priority)
- `10-19`: GeneralUser support components
- `20-29`: GeneralUser advanced features
- `30-39`: CommunityMember components
- `40-49`: AdminAccess components

---

## Priority-Based Implementation Order

Based on **REQ-000b_Scope.md** performance criteria and business value:

### Phase 1: Core Plant Database

**Priority**: CRITICAL - Foundation for entire system

1. `req-01-general-user-plant-database.md`
2. `req-02-general-user-plant-search.md`
3. `req-03-general-user-plant-filter.md`

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

4. `req-04-general-user-calculations.md`
5. `req-05-general-user-usda-zones.md`

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

6. `req-10-general-user-weather.md`
7. `req-11-general-user-notifications.md`
8. `req-12-general-user-general-resources.md`

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

9. `req-13-general-user-feedback.md`
10. `req-20-general-user-account-favorites.md`
11. `req-21-general-user-add-plant.md`

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

12. `req-22-general-user-moon-gardening.md`
13. `req-06-general-user-pest-database.md`

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

14. `req-30-community-member-announcements.md`
15. `req-31-community-member-plot-management.md`
16. `req-32-community-member-team-chores.md`
17. `req-33-community-member-apprentice-program.md`

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

18. `req-40-admin-account-management.md`
19. `req-41-admin-educator-role.md`
20. `req-42-admin-elevated-access.md`

**Why Last:**

- Highest security risk
- Serves smallest user segment
- Can be handled manually initially

**Performance Criteria:**

- Create/manage community leads - [account management](../../requirements/REQ-000b_Scope.md#starting-deliverable--account-management)
- Assign roles and permissions
- View/manage all accounts - [elevated view access](../../requirements/REQ-000b_Scope.md#starting-deliverable--elevated-view-access)

---

## Requirements Files to Generate

### Phase 1: Core Plant Database (3 files)

#### 1. `req-01-general-user-plant-database.md`

**Scope**: Plant data model, storage, and basic display

**Key Sections:**

- **Context**: Foundation of entire system, used by all users for plant information

- **Functional Requirements**:

    - Display plant details (common name, scientific name, USDA zones, etc.)
    - Support for multiple plant types (annual, perennial, shrub, tree, vine)
    - Track physical attributes (spacing, height, container size)
    - Store companion plant relationships
    - Track medicinal benefits and uses

- **Data Requirements**:

    - Plant model schema (see `2024-Django-Attempt/Plants/models.py:21-104` for reference)
    - Required fields vs optional fields
    - Data validation rules (CodeGuard)
    - Hardiness zone categories (1a-13b)
    - Exposure categories (Full Sun, Partial Sun, Partial Shade, Shade)

- **Integration Requirements**:

    - Database schema (SQLite initially, PostgreSQL-compatible)
    - API endpoints for plant CRUD operations
    - Data seeding/migration strategy

- **Constraints**:

    - Python 3.12+, Django backend
    - HTMX frontend (not React/Next.js initially)
    - Tailwind CSS
    - Platform independent database design

- **Success Criteria**:

    - Plant data displays correctly
    - Data validation prevents invalid entries (CodeGuard)
    - API endpoints return expected JSON
    - Database queries perform efficiently

**CodeGuard Focus**: Input validation, SQL injection prevention, data sanitization

**Maps to REQ-000b**: [`System.GenUser.ViewsAndInsights.PlantDatabase`](../../requirements/REQ-000b_Scope.md#starting-deliverable--plant-database)

---

#### 2. `req-02-general-user-plant-search.md`

**Scope**: Search functionality for finding plants by name

**Key Sections:**

- **Context**: Primary discovery mechanism, used by all user types

- **Functional Requirements**:

    - Search by common name (partial match)
    - Search by scientific name (partial match)
    - Case-insensitive matching
    - Display search results with pagination
    - Handle "no results found" gracefully
    - Maintain search state across sessions

- **UI/UX Requirements**:

    - Search input field (accessible, keyboard navigation)
    - Real-time search suggestions (debounced)
    - Results display with plant preview cards
    - Responsive design (mobile, tablet, desktop)
    - Loading states and error messages
    - WCAG 2.1 Level AA compliance

- **Data Requirements**:

    - Search indexing strategy (full-text search)
    - Query optimization for large datasets
    - Result ranking algorithm

- **Integration Requirements**:

    - Integrates with Plant Database component
    - API endpoint: `GET /api/plants/search?q={query}`
    - Frontend component in `src/components/PlantSearch`

- **Constraints**:

    - Response time < 500ms for 10,000+ plants
    - Mobile-first design
    - Keyboard accessible
    - No external search services (self-hosted)

- **Success Criteria**:

    - Search returns relevant results
    - Performance meets < 500ms requirement
    - Accessibility tests pass with screen reader
    - Error handling works for all edge cases

**CodeGuard Focus**: XSS prevention, input sanitization, query injection prevention

**Maps to REQ-000e**: `OR1.1`, `OR1.2`, `MULTI` (msg_plant_404)

---

#### 3. `req-03-general-user-plant-filter.md`

**Scope**: Advanced filtering by plant characteristics, zones, timing

**Key Sections:**

- **Context**: Helps users find plants matching specific criteria (zone, type, season, benefits)

- **Functional Requirements**:

    - Filter by USDA hardiness zone (single or range)
    - Filter by plant type (annual, perennial, shrub, tree, vine)
    - Filter by exposure (Full Sun, Partial Sun, Shade, etc.)
    - Filter by characteristics (drought tolerant, deer resistant, pollinator friendly)
    - Filter by planting season/timing
    - Combine multiple filters (AND logic vs OR logic)
    - Show/hide applied filters
    - Clear all filters option
    - Save filter preferences

- **UI/UX Requirements**:

    - Filter panel (sidebar or modal)
    - Filter chips showing active filters
    - Filter count badges
    - Responsive filter UI
    - Accessible filter controls (ARIA labels)
    - Visual feedback when filters applied

- **Data Requirements**:

    - Efficient database indexing for filter fields
    - Filter state management
    - Filter persistence (local storage or user account)

- **Integration Requirements**:

    - Integrates with Plant Database and Plant Search
    - API endpoint: `GET /api/plants/filter?zone={zone}&type={type}&...`
    - Frontend component in `src/components/PlantFilter`

- **Constraints**:

    - Filter performance < 500ms
    - Support 10+ simultaneous filters
    - Mobile-friendly filter UI

- **Success Criteria**:

    - Filters return correct results
    - AND vs OR logic works as expected
    - Filter state persists across sessions
    - Performance requirements met
    - Accessibility requirements met

**CodeGuard Focus**: Input validation, query parameter sanitization, authorization checks

**Maps to REQ-000e**: `OR2.1` (filter_any), `OR2.2` (filter_exact)

---

### Phase 2: Supporting Calculations & Data (2 files)

#### 4. `req-04-general-user-calculations.md`

**Scope**: Frost date calculations, planting date recommendations

**Key Sections:**

- **Context**: Critical for location-based planting guidance

- **Functional Requirements**:

    - Calculate first/last frost dates from USDA zone
    - Calculate planting dates based on frost dates and plant requirements
    - Calculate germination timelines
    - Calculate days to harvest
    - Provide "weeks before/after frost" calculations

- **Data Requirements**:

    - USDA zone to frost date mapping table
    - Plant germination and maturity data
    - Date calculation algorithms

- **Integration Requirements**:

    - Integrates with Plant Database
    - Integrates with USDA Zones component
    - API endpoint: `GET /api/calculate/frost-dates?zone={zone}`

- **Constraints**:

    - Calculation accuracy ±3 days
    - Support all USDA zones (1a-13b)
    - Handle edge cases (no frost zones, year-round growing)

- **Success Criteria**:

    - Frost dates accurate for all zones
    - Planting date calculations correct
    - Edge cases handled gracefully

**CodeGuard Focus**: Input validation, date handling security

**Maps to REQ-000b**: [`System.GenUser.ViewsAndInsights.Calculations`](../../requirements/REQ-000b_Scope.md#starting-deliverable--calculations)

---

#### 5. `req-05-general-user-usda-zones.md`

**Scope**: USDA hardiness zone data and location mapping

**Key Sections:**

- **Context**: Foundation for all location-based features

- **Functional Requirements**:

    - Store USDA zone data (1a-13b)
    - Map user location (GPS or manual) to USDA zone
    - Provide zone descriptions and temperature ranges
    - Support zone-based plant filtering
    - Allow manual zone selection (privacy-conscious users)

- **Data Requirements**:

    - USDA zone reference table
    - Location to zone mapping (geospatial data)
    - Zone temperature range data

- **Integration Requirements**:

    - Integrates with Plant Database, Calculations, Weather
    - API endpoint: `GET /api/zones/{zone}`
    - Geolocation service integration (optional)

- **Constraints**:

    - Support US zones initially, expandable to other countries
    - Privacy-first (location optional)
    - Fast zone lookup (< 100ms)

- **Success Criteria**:

    - Accurate zone determination
    - Manual override works
    - Privacy requirements met

**CodeGuard Focus**: Location data privacy, input validation

**Maps to REQ-000b**: [Multiple use cases requiring zone data](../../requirements/REQ-000b_Scope.md#primary-deliverable--general-user-access)

---

### Phase 3: User Experience Enhancements (3 files)

#### 6. `req-10-general-user-weather.md`

**Scope**: Weather data integration, alerts, and protection planning

**Key Sections:**

- **Context**: Protects user plants from weather damage

- **Functional Requirements**:

    - Connect to weather API (OpenWeather, Weather.gov, etc.)
    - Display current weather conditions
    - Display weather forecast (7-day)
    - Generate protection alerts (frost, extreme heat, heavy rain)
    - Show historical weather data
    - Provide planting recommendations based on weather
    - Configurable notification thresholds

- **UI/UX Requirements**:

    - Weather widget (current conditions)
    - Forecast display (daily/hourly)
    - Alert banners (urgent warnings)
    - Responsive design
    - Accessible weather icons and data

- **Data Requirements**:

    - Weather API integration (rate limits, caching)
    - Historical weather data storage
    - Alert threshold configuration

- **Integration Requirements**:

    - Integrates with USDA Zones, Notifications
    - Weather API: OpenWeather, Weather.gov, or similar
    - API endpoint: `GET /api/weather?location={lat,lon}`
    - Cache weather data (2 requests/hour limit)

- **Constraints**:

    - Free tier API usage (or user-provided API key)
    - 2 requests/hour rate limit (system default)
    - Graceful degradation if API unavailable
    - Privacy-conscious (location optional)

- **Success Criteria**:

    - Weather data displays accurately
    - Alerts trigger correctly
    - API rate limits respected
    - Offline mode works with cached data

**CodeGuard Focus**: API key security, rate limiting, external API validation

**Maps to REQ-000b**: [`System.GenUser.Weather`](../../requirements/REQ-000b_Scope.md#weather) (14 performance criteria)

---

#### 7. `req-11-general-user-notifications.md`

**Scope**: User notification preferences and delivery

**Key Sections:**

- **Context**: Keeps users informed of weather, system updates, community events

- **Functional Requirements**:

    - Notification preferences (weather, community, system)
    - Notification delivery (in-app, email, push)
    - Notification history/inbox
    - Mark as read/unread
    - Notification scheduling (daily digest, immediate)
    - Opt-in/opt-out per notification type

- **UI/UX Requirements**:

    - Notification bell icon with badge count
    - Notification panel/dropdown
    - Settings page for preferences
    - Accessible notification UI

- **Data Requirements**:

    - User notification preferences table
    - Notification queue/history
    - Delivery status tracking

- **Integration Requirements**:

    - Integrates with Weather, Community features
    - Email service integration (SendGrid, Mailgun, etc.)
    - Push notification service (optional)

- **Constraints**:

    - Privacy-first (opt-in by default)
    - Email rate limits
    - Notification delivery < 5 minutes

- **Success Criteria**:

    - Preferences save correctly
    - Notifications deliver as configured
    - Unsubscribe works reliably

**CodeGuard Focus**: Email security, subscription management, spam prevention

**Maps to REQ-000b**: [`System.GenUser.Notifications`](../../requirements/REQ-000b_Scope.md#notifications) (10 performance criteria)

---

#### 8. `req-12-general-user-general-resources.md`

**Scope**: Curated gardening resources and affiliate links

**Key Sections:**

- **Context**: Helps users improve gardening knowledge and access tools

- **Functional Requirements**:

    - Display curated resource list (USDA, extension offices, etc.)
    - Categorize resources (beginner, advanced, topics)
    - Affiliate links with proper disclosure
    - External link tracking (analytics)
    - Resource search and filtering

- **UI/UX Requirements**:

    - Resource cards with descriptions
    - Category filters
    - External link indicators
    - Affiliate link disclosures (FTC compliance)
    - Responsive layout

- **Data Requirements**:

    - Resource database (title, URL, description, category)
    - Affiliate link tracking
    - Click analytics

- **Integration Requirements**:

    - Content management for resources
    - Analytics integration (privacy-focused)

- **Constraints**:

    - FTC affiliate disclosure compliance
    - Privacy-focused analytics (no PII)
    - Accessible external link handling

- **Success Criteria**:

    - Resources display correctly
    - Affiliate disclosures clear
    - External links open safely

**CodeGuard Focus**: XSS prevention (user-generated links), affiliate tracking security

**Maps to REQ-000b**: [`System.GenUser.GeneralResources`](../../requirements/REQ-000b_Scope.md#general-resources)

---

### Phase 4: User Data & Feedback (3 files)

#### 9. `req-13-general-user-feedback.md`

**Scope**: User feedback, bug reports, feature requests, plant submissions

**Key Sections:**

- **Context**: Continuous improvement and community engagement

- **Functional Requirements**:

    - Feedback submission form
    - Bug report form (with screenshot upload)
    - Feature request submission
    - Plant addition request form
    - View known bugs list (public issue tracker)
    - Email fallback option
    - Automatic GitHub issue creation (optional)

- **UI/UX Requirements**:

    - Accessible forms (WCAG 2.1 AA)
    - Form validation with helpful error messages
    - File upload (screenshots, max 5MB)
    - Thank you confirmation
    - Issue status tracking (optional)

- **Data Requirements**:

    - Feedback/bug submission table
    - File upload storage (S3, local, etc.)
    - Issue categorization (bug, feature, plant request)
    - Duplicate detection

- **Integration Requirements**:

    - GitHub Issues API integration (optional)
    - Email service for notifications
    - File storage service

- **Constraints**:

    - File upload size limit (5MB)
    - Rate limiting (spam prevention)
    - Anonymous submissions allowed (privacy)
    - CAPTCHA for spam prevention (privacy-focused)

- **Success Criteria**:

    - Forms submit successfully
    - File uploads work correctly
    - Spam prevention effective
    - GitHub integration works (if enabled)

**CodeGuard Focus**: File upload security, XSS prevention, CSRF protection, spam prevention

**Maps to REQ-000b**: [`System.GenUser.Feedback`](../../requirements/REQ-000b_Scope.md#user-feedback) (6 starting deliverables)

---

#### 10. `req-20-general-user-account-favorites.md`

**Scope**: Save favorite plants, backup data, account sync

**Key Sections:**

- **Context**: Personalization and data portability

- **Functional Requirements**:

    - Save favorite plants (local storage)
    - Create user account (optional, OAuth)
    - Sync favorites to cloud account
    - Export favorites to file (JSON, CSV)
    - Import favorites from file
    - Manage saved plants (add, remove, organize)

- **UI/UX Requirements**:

    - Favorite button/icon (heart, star)
    - Favorites list view
    - Account creation/login UI
    - Data export/import UI
    - Accessible controls

- **Data Requirements**:

    - User favorites table (user_id, plant_id)
    - Local storage schema
    - Cloud sync mechanism
    - Export file format (JSON)

- **Integration Requirements**:

    - OAuth providers (Google, GitHub, etc.)
    - User authentication system
    - Cloud storage sync

- **Constraints**:

    - Privacy-first (local storage default)
    - OAuth optional (no forced login)
    - Data export standard format (JSON)
    - GDPR compliance (data portability)

- **Success Criteria**:

    - Favorites save locally
    - Account sync works correctly
    - Export/import successful
    - Privacy requirements met

**CodeGuard Focus**: OAuth security, session management, data export security

**Maps to REQ-000b**: [`System.GenUser.AccountFavorites`](../../requirements/REQ-000b_Scope.md#account-favorites) (5 performance criteria)

---

#### 11. `req-21-general-user-add-plant.md`

**Scope**: User-contributed plant submissions for database

**Key Sections:**

- **Context**: Community-driven database expansion

- **Functional Requirements**:

    - Plant submission form (all required fields)
    - Data validation (plant name uniqueness check)
    - Submission review workflow (admin approval)
    - Duplicate detection
    - Submission status tracking (pending, approved, rejected)
    - User notification on status change

- **UI/UX Requirements**:

    - Multi-step plant submission form
    - Field validation with helpful messages
    - Preview before submit
    - Submission history (for logged-in users)
    - Accessible form controls

- **Data Requirements**:

    - Plant submission table (pending_plants)
    - Approval workflow
    - Duplicate detection algorithm (fuzzy matching)

- **Integration Requirements**:

    - Integrates with Plant Database
    - Admin approval interface
    - Email notifications

- **Constraints**:

    - Submission rate limiting (spam prevention)
    - Required fields enforced
    - Image uploads optional (max 5MB)
    - Admin approval required before publication

- **Success Criteria**:

    - Submissions save correctly
    - Duplicate detection works
    - Approval workflow functions
    - Notifications sent correctly

**CodeGuard Focus**: Input validation, duplicate prevention, approval workflow security

**Maps to REQ-000b**: [`System.GenUser.AddPlant`](../../requirements/REQ-000b_Scope.md#add-plant) (8 performance criteria)

---

### Phase 5: Advanced General Features (2 files)

#### 12. `req-22-general-user-moon-gardening.md`

**Scope**: Moon phase calculations and planting suggestions

**Key Sections:**

- **Context**: Traditional gardening practice based on lunar cycles

- **Functional Requirements**:

    - Calculate current moon phase
    - Display moon phase calendar (monthly view)
    - Provide planting suggestions by moon phase
    - Explain moon phase gardening principles
    - Show next new moon/full moon dates
    - Historical moon phase lookup

- **UI/UX Requirements**:

    - Moon phase widget (current phase)
    - Monthly calendar with phases
    - Suggestion cards by phase
    - Educational content
    - Accessible moon phase icons

- **Data Requirements**:

    - Moon phase calculation algorithm
    - Planting suggestion database (by phase)
    - Educational content

- **Integration Requirements**:

    - Integrates with Calculations component
    - Date/time library for astronomical calculations

- **Constraints**:

    - Calculation accuracy ±1 day
    - Works for any location (latitude/longitude)
    - Educational and optional (not prescriptive)

- **Success Criteria**:

    - Moon phases calculated accurately
    - Suggestions helpful and accurate
    - Educational content clear

**CodeGuard Focus**: Date/time security, input validation

**Maps to REQ-000b**: [`System.GenUser.MoonGardening`](../../requirements/REQ-000b_Scope.md#moon-based-gardening) (5 starting deliverables)

---

#### 13. `req-06-general-user-pest-database.md`

**Scope**: Common garden pests, identification, organic treatments

**Key Sections:**

- **Context**: Helps gardeners identify and treat pests organically

- **Functional Requirements**:

    - Pest database (name, description, images, affected plants)
    - Pest identification guide (symptoms, photos)
    - Organic treatment options
    - Prevention strategies
    - Search pests by name or affected plant
    - Filter by pest type (insect, disease, animal)

- **UI/UX Requirements**:

    - Pest cards with images
    - Identification wizard (symptom-based)
    - Treatment recommendations
    - Accessible pest information

- **Data Requirements**:

    - Pest database schema
    - Plant-to-pest relationships
    - Treatment database
    - Image storage

- **Integration Requirements**:

    - Integrates with Plant Database
    - Image storage service

- **Constraints**:

    - Focus on organic/sustainable treatments
    - Evidence-based recommendations
    - Image size limits (optimization)

- **Success Criteria**:

    - Pest data accurate
    - Identification wizard helpful
    - Treatment recommendations effective

**CodeGuard Focus**: Image upload security, content validation

**Maps to REQ-000b**: [`System.GenUser.ViewsAndInsights.PestDatabase`](../../requirements/REQ-000b_Scope.md#starting-deliverable--pest-database) (TBD in scope doc)

---

### Phase 6: Community Features (4 files)

#### 14. `req-30-community-member-announcements.md`

**Scope**: Community bulletin board, workday planning, notifications

**Key Sections:**

- **Context**: Secure communication for community garden members

- **Functional Requirements**:

    - Create community announcements (title, description, dates, POC)
    - Announcement types (general, compost, team-specific, training)
    - Announcement expiration (auto-delete after end date)
    - Announcement filtering (by type, team, date)
    - Workday list (add, edit, mark complete)
    - Announcement notifications (opt-in)
    - Weather announcements (auto-generated, manual override)

- **UI/UX Requirements**:

    - Announcement board (card layout)
    - Announcement creation form
    - Visual indicators for announcement types
    - Workday task list
    - Accessible UI

- **Data Requirements**:

    - Announcement table (community_id, type, dates, content)
    - Workday tasks table
    - Notification preferences

- **Integration Requirements**:

    - Integrates with Community Member authentication
    - Integrates with Notifications component
    - Role-based access control (RBAC)

- **Constraints**:

    - Community-specific access (security critical)
    - Auto-expiration enforced
    - Weather announcements auto-delete after 24h
    - Announcement editing limited to creator or community lead

- **Success Criteria**:

    - Announcements display correctly
    - Permissions enforced correctly
    - Auto-expiration works
    - Notifications sent correctly

**CodeGuard Focus**: Authorization, RBAC, XSS prevention, CSRF protection

**Maps to REQ-000b**: [`System.CommunityMember.Announcements`](../../requirements/REQ-000b_Scope.md#announcements) (18 performance criteria)

---

#### 15. `req-31-community-member-plot-management.md`

**Scope**: Plot assignment, support requests, plot tracking

**Key Sections:**

- **Context**: Coordinate plot management in community gardens

- **Functional Requirements**:

    - View available plots
    - Request plot management (gardeners/apprentices only)
    - Request plot support (all members)
    - Approve/deny plot requests (mentor team, plot managers)
    - Release plot (current manager)
    - Track plot assignments
    - Plot details (location, size, manager, supporters)
    - Support request announcements
    - Plot vacancy announcements

- **UI/UX Requirements**:

    - Plot grid/map view
    - Plot details modal
    - Request forms
    - Request status tracking
    - Approval interface (for authorized roles)
    - Accessible UI

- **Data Requirements**:

    - Plot table (plot_id, community_id, location, size, status)
    - Plot assignments table (plot_id, user_id, role, status)
    - Request tracking table

- **Integration Requirements**:

    - Integrates with Community Member authentication
    - Integrates with Announcements component
    - Role-based access control

- **Constraints**:

    - Only gardeners/apprentices manage plots
    - Only members/supporters can support plots
    - Approval workflow enforced
    - Notifications on status changes

- **Success Criteria**:

    - Plot assignments correct
    - Request workflow functions
    - Permissions enforced
    - Notifications sent

**CodeGuard Focus**: Authorization, RBAC, data validation, approval workflow security

**Maps to REQ-000b**: [`System.CommunityMember.PlotAssignment`](../../requirements/REQ-000b_Scope.md#plot-assignment-system) (20 performance criteria)

---

#### 16. `req-32-community-member-team-chores.md`

**Scope**: Team assignments, chore tracking, hour logging

**Key Sections:**

- **Context**: Coordinate community garden teams and chores

- **Functional Requirements**:

    - View team assignments (compost, mentoring, communications, delivery, etc.)
    - View chore assignments
    - Track hours for teams/chores
    - View team members (privacy-aware)
    - Compost team: create/edit compost events
    - Delivery team: self-assign delivery slots
    - Communications team: create announcements with notifications
    - Mentor team: assign mentors to mentees

- **UI/UX Requirements**:

    - Team directory (privacy-aware)
    - Chore board
    - Hour tracking interface
    - Team-specific dashboards
    - Accessible UI

- **Data Requirements**:

    - Team table (team_id, community_id, team_name)
    - Team assignments table (user_id, team_id, role)
    - Chore table (chore_id, community_id, chore_name)
    - Hour tracking table (user_id, team_id, chore_id, hours, date)

- **Integration Requirements**:

    - Integrates with Community Member authentication
    - Integrates with Announcements, Notifications
    - Role-based access control

- **Constraints**:

    - Privacy controls (opt-in visibility)
    - Team-specific permissions
    - Hour tracking accuracy

- **Success Criteria**:

    - Team assignments display correctly
    - Hour tracking works
    - Team-specific features function
    - Privacy controls enforced

**CodeGuard Focus**: Authorization, RBAC, privacy controls, data validation

**Maps to REQ-000b**: [`System.CommunityMember.TeamAndChores`](../../requirements/REQ-000b_Scope.md#team--chores) (17 performance criteria)

---

#### 17. `req-33-community-member-apprentice-program.md`

**Scope**: Apprentice training tracking, mentor assignments, progress monitoring

**Key Sections:**

- **Context**: Structured training program for new community gardeners

- **Functional Requirements**:

    - Training module library (community-specific)
    - Training progress tracking (per apprentice)
    - Mark training tasks complete
    - Mentor assignment (1:1)
    - Mentor progress viewing (opt-in by apprentice)
    - Training announcements (required vs optional)
    - Transition apprentice to gardener (mentor team action)
    - Educator role: create/edit training content

- **UI/UX Requirements**:

    - Training module list (with progress indicators)
    - Training content viewer
    - Progress dashboard
    - Mentor assignment interface
    - Privacy controls (share progress with mentor)
    - Accessible UI

- **Data Requirements**:

    - Training modules table (module_id, community_id, content, required/optional)
    - Progress tracking table (user_id, module_id, status, completion_date)
    - Mentor assignments table (mentor_id, mentee_id, community_id)

- **Integration Requirements**:

    - Integrates with Community Member authentication
    - Integrates with Announcements component
    - Role-based access control (educator, mentor team)

- **Constraints**:

    - Community-specific training content
    - Privacy-first (progress sharing opt-in)
    - Mentor team approval for role transitions

- **Success Criteria**:

    - Training content displays correctly
    - Progress tracking accurate
    - Mentor assignments work
    - Privacy controls enforced
    - Role transitions function correctly

**CodeGuard Focus**: Authorization, RBAC, privacy controls, content security

**Maps to REQ-000b**: [`System.CommunityMember.ApprenticeProgram`](../../requirements/REQ-000b_Scope.md#apprentice-program) (7 performance criteria)

---

### Phase 7: Admin Features (3 files)

**NOTE**: These are currently de-prioritized per REQ-000b. Generate only after all higher-priority requirements are complete and implemented.

#### 18. `req-40-admin-account-management.md`

**Scope**: System admin and community lead account management

**Key Sections:**

- **Context**: User administration and community governance

- **Functional Requirements**:

    - System admin: create/lock community lead accounts
    - System admin: mark any account inactive (community-specific)
    - Community lead: mark community members inactive
    - Community lead: assign teams and chores
    - Community lead: view apprentice progress (if permitted)
    - Role transition management
    - Inactive account permissions (downgrade to general user)

- **UI/UX Requirements**:

    - Admin dashboard
    - User management table (search, filter, sort)
    - Role assignment interface
    - Account status management
    - Audit log viewer

- **Data Requirements**:

    - User roles table (user_id, community_id, role, status)
    - Audit log table (action, user_id, timestamp, details)
    - Permission inheritance model

- **Integration Requirements**:

    - Integrates with all Community Member components
    - Role-based access control (highest privilege level)

- **Constraints**:

    - Two-factor authentication required for admins (CodeGuard)
    - Audit logging mandatory (security)
    - Account lockout after failed attempts
    - Session timeout for admin accounts

- **Success Criteria**:

    - Account management functions correctly
    - Permissions enforced strictly
    - Audit log complete and accurate
    - Security requirements met (CodeGuard)

**CodeGuard Focus**: Authentication, authorization, session management, audit logging, privilege escalation prevention

**Maps to REQ-000b**: [`System.AdminAccess.AccountManagement`](../../requirements/REQ-000b_Scope.md#starting-deliverable--account-management) (6 performance criteria)

---

#### 19. `req-41-admin-educator-role.md`

**Scope**: Educator role for training content management

**Key Sections:**

- **Context**: Specialized role for creating/managing training programs

- **Functional Requirements**:

    - View all training content
    - Create new training modules
    - Edit existing training modules
    - Delete training modules (with confirmation)
    - Mark trainings as required or optional
    - Assign educators (community lead, mentor team, system admin)

- **UI/UX Requirements**:

    - Training content management dashboard
    - Training module editor (rich text, images, video embeds)
    - Required/optional toggle
    - Preview mode
    - Accessible UI

- **Data Requirements**:

    - Educator role assignment
    - Training content versioning
    - Training content approval workflow

- **Integration Requirements**:

    - Integrates with Apprentice Program component
    - Role-based access control

- **Constraints**:

    - Educator role inherits community member permissions
    - Community lead automatically has educator role
    - Mentor team automatically has educator role

- **Success Criteria**:

    - Content creation/editing works
    - Role assignment correct
    - Content displays correctly in apprentice program

**CodeGuard Focus**: Authorization, content validation, XSS prevention

**Maps to REQ-000b**: [`System.AdminAccess.CommunityEducatorRole`](../../requirements/REQ-000b_Scope.md#starting-deliverable--community-educator-role) (5 performance criteria)

---

#### 20. `req-42-admin-elevated-access.md`

**Scope**: Elevated viewing and impersonation for troubleshooting

**Key Sections:**

- **Context**: Admin and community lead troubleshooting capabilities

- **Functional Requirements**:

    - System admin: view all accounts
    - Community lead: view all community accounts
    - Community lead: view community as specific role (impersonation)
    - Community lead: engage as specific role (impersonation)
    - Mentor team: view mentee progress (if permitted)
    - Audit logging for all elevated access
    - Session recording for impersonation (security)

- **UI/UX Requirements**:

    - Admin view toggle
    - Role impersonation UI (with clear indicators)
    - Impersonation session banner
    - Exit impersonation control
    - Accessible UI

- **Data Requirements**:

    - Impersonation session tracking
    - Audit log for elevated access
    - Role hierarchy model

- **Integration Requirements**:

    - Integrates with all components
    - Highest-level RBAC

- **Constraints**:

    - Impersonation audit logged (who, when, what role, duration)
    - Impersonation session timeout (30 minutes)
    - Cannot impersonate system admin
    - Two-factor authentication required

- **Success Criteria**:

    - Impersonation works correctly
    - Audit logging complete
    - Security requirements met (CodeGuard)
    - Session management secure

**CodeGuard Focus**: Audit logging, session management, privilege escalation prevention, impersonation security

**Maps to REQ-000b**: [`System.AdminAccess.ElevatedViewAccess`](../../requirements/REQ-000b_Scope.md#starting-deliverable--elevated-view-access) (5 performance criteria)

---

## Agents and Prompts to Use

### Workflow Automation

The project has established **workflow prompts** that automate multi-step processes:

#### Primary Workflow: Requirements → Specification

**Prompt**: `.github/prompts/workflow-requirements-to-spec.prompt.md`

**Slash Command**: `/make-spec-from-req <req-file> [scope]`

**What it does:**

1. Reads the requirement file
2. Generates a detailed specification using `spec-template.md`
3. Creates architecture diagrams (Text + ASCII + Mermaid)
4. Creates threat model using STRIDE methodology
5. Runs quality review checklist
6. Updates cross-reference table

**Example usage:**

```
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-01-general-user-plant-database.md
```

**Outputs:**

- `docs/specifications/spec-01-general-user-plant-database.md`
- `docs/diagrams/arch-01-general-user-plant-database.md`
- `docs/diagrams/threat-01-general-user-plant-database.md`
- Updated `docs/SPEC-CROSS-REFERENCE.md`

---

#### Secondary Workflow: Specification → Code

**Prompt**: `.github/prompts/workflow-spec-to-code.prompt.md`

**Slash Command**: `/implement-spec <spec-file>`

**What it does:**

1. Reads the specification file
2. Implements using TDD workflow (Red → Green → Refactor)
3. Runs security review with CodeGuard
4. Runs quality validation checklist
5. Updates cross-reference table

**Example usage:**

```
Execute the workflow-spec-to-code prompt for docs/specifications/spec-01-general-user-plant-database.md
```

**Outputs:**

- Source files (e.g., `src/plants/models.py`, `src/plants/views.py`)
- Test files (e.g., `tests/test_plants.py`)
- Updated `docs/SPEC-CROSS-REFERENCE.md`

---

### Individual Prompts (for granular control)

If you need to run individual steps instead of full workflows:

| Prompt | Purpose | Slash Command |
|--------|---------|---------------|
| `create-requirement.prompt.md` | Create new requirement from scratch | `/create-requirement <name>` |
| `generate-spec-from-requirement.prompt.md` | Generate spec only (no diagrams/threat model) | N/A (use workflow instead) |
| `create-architecture-diagram.prompt.md` | Generate architecture diagram only | `/create-architecture <spec>` |
| `create-threat-model.prompt.md` | Generate threat model only (STRIDE) | `/create-threat-model <spec>` |
| `generate-code-from-spec.prompt.md` | Generate code only (no TDD) | N/A (use workflow instead) |
| `security-review.prompt.md` | Run CodeGuard security review | `/security-review <module>` |
| `verify-implementation.prompt.md` | Comprehensive verification | `/verify <module>` |
| `update-documentation.prompt.md` | Update documentation indexes | `/update-docs <type> <files>` |

---

### Agent Usage

The project supports specialized agents via the `Task` tool:

#### Explore Agent (for research)

**When to use**: Understanding codebase structure before creating requirements

**Example**:

```
Use the Task tool with subagent_type='Explore' to analyze the existing Plant model in 2024-Django-Attempt/Plants/models.py and identify all fields that should be included in req-01-general-user-plant-database.md
```

**Thoroughness levels**: `quick`, `medium`, `very thorough`

---

#### Plan Agent (for architecture planning)

**When to use**: Designing implementation strategy before writing specs

**Example**:

```
Use the Task tool with subagent_type='Plan' to design the plant search API architecture for req-02-general-user-plant-search.md
```

---

### Recommended Agent Sequence for Each Requirement

For each requirement file to be generated:

1. **Research Phase** (Explore Agent):
   ```
   Use Explore agent to analyze REQ-000b section for [component name] and identify all performance criteria and data needs
   ```

2. **Requirements Generation Phase** (Manual or `/create-requirement`):
   ```
   /create-requirement [component-name]
   ```
   Then manually fill in details following the template.

3. **Specification Generation Phase** (Workflow Prompt):
   ```
   Execute the workflow-requirements-to-spec prompt for docs/requirements/req-[XX]-[component].md
   ```

4. **Implementation Phase** (Workflow Prompt):
   ```
   Execute the workflow-spec-to-code prompt for docs/specifications/spec-[XX]-[component].md
   ```

---

## CodeGuard Integration

**Plugin**: `codeguard-security@project-codeguard`

**Documentation**: https://project-codeguard.org/

**Update command**: `/plugin update codeguard-security@project-codeguard`

### Security Coverage Areas

CodeGuard provides security rules across 8 domains. Each requirement file must include security considerations in the **Security Considerations** section:

1. **Cryptography**
   - Relevant for: Account Favorites, Community Member authentication
   - Requirements: Secure password storage (bcrypt/Argon2), HTTPS only, no hardcoded secrets

2. **Input Validation**
   - Relevant for: ALL requirements (especially user input forms)
   - Requirements: Server-side validation, SQL injection prevention, XSS prevention, command injection prevention

3. **Authentication**
   - Relevant for: Account Favorites, all Community Member requirements, Admin requirements
   - Requirements: MFA for admin, OAuth/OIDC for user accounts, secure session management, password requirements

4. **Authorization**
   - Relevant for: Community Member requirements, Admin requirements
   - Requirements: RBAC implementation, principle of least privilege, role inheritance model, permission checks at API and UI layers

5. **Supply Chain Security**
   - Relevant for: ALL requirements (dependency management)
   - Requirements: Dependency scanning, SBOM generation, pinned versions

6. **Cloud Security**
   - Relevant for: Weather API, file uploads, cloud storage
   - Requirements: API key security, rate limiting, secure file storage

7. **Platform Security**
   - Relevant for: ALL requirements
   - Requirements: Security headers, CSRF protection, secure cookies, security.txt

8. **Data Protection**
   - Relevant for: ALL requirements (especially PII)
   - Requirements: Data minimization, encryption at rest/transit, GDPR compliance, privacy controls

### CodeGuard in Requirements Template

The template section **Security Considerations** (lines 380-395) includes:

```markdown
### Security Considerations

Ensure we are also using CodeGuard rules for security best practices! Including but not limited to:

- **Input Sanitization:** How should user input be sanitized?
- **Authentication:** Does this require authentication? What method?
- **Authorization:** What permissions are required? Role-based access?
- **Data Privacy:** What sensitive data must be protected?
- **Encryption:** At rest? In transit?
- **Vulnerability Mitigation:** SQL injection, XSS, CSRF, command injection, etc.
- **Secret Management:** How are secrets stored and accessed?
- **Audit Logging:** What actions need to be logged?
- **XSS Prevention:** What measures prevent cross-site scripting?
- **CSRF Protection:** Is CSRF protection needed?
- **CodeGuard Rules:** ALWAYS utilize CodeGuard rules for secure coding practices
```

### CodeGuard in Threat Models

Every specification will have an associated threat model (`.github/prompts/create-threat-model.prompt.md`) using **STRIDE methodology**:

- **S**poofing (Authentication)
- **T**ampering (Data Integrity)
- **R**epudiation (Audit Logging)
- **I**nformation Disclosure (Data Privacy)
- **D**enial of Service (Availability)
- **E**levation of Privilege (Authorization)

Threat models will reference CodeGuard rules for mitigation strategies.

### CodeGuard Review Process

After code generation, run:

```
/security-review <module-path>
```

This executes `.github/prompts/security-review.prompt.md` which:
1. Analyzes code against CodeGuard rules
2. Identifies security vulnerabilities
3. Provides remediation recommendations
4. Generates security review report

---

## Workflow Execution Plan

### Step-by-Step Execution

#### Prerequisites

1. **Environment Setup**:
   ```bash
   /setup-env
   ```

2. **Review Templates**:
    - `docs/templates/requirements-template.md`
    - `docs/templates/spec-template.md` (still needs to be reviewed to merge with additional file)

3. **Understand REQ-000 Series**:
    - Read `docs/requirements/REQ-000a_General.md`
    - Read `docs/requirements/REQ-000b_Scope.md`
    - Read `docs/requirements/REQ-000c_UseCases.md`

---

#### Phase 1: Core Plant Database

**Requirement 1: Plant Database**

1. **Generate Requirement**:
    ```
    Execute .github/prompts/create-requirement.prompt.md for "general-user-plant-database"
    ```

    Output: `docs/requirements/req-01-general-user-plant-database.md`

2. **Manual Review**:
    - Verify all sections complete
    - Cross-reference with REQ-000b: `System.GenUser.ViewsAndInsights.PlantDatabase`
    - Add CodeGuard security considerations
    - Review data model against `2024-Django-Attempt/Plants/models.py`

3. **Generate Specification**:
    ```
    Execute .github/prompts/workflow-requirements-to-spec.prompt.md for docs/requirements/req-01-general-user-plant-database.md
    ```

    Outputs:

    - `docs/specifications/spec-01-general-user-plant-database.md`
    - `docs/diagrams/arch-01-general-user-plant-database.md`
    - `docs/diagrams/threat-01-general-user-plant-database.md`

4. **Manual Review**:

    - Verify three diagram formats (Text, ASCII, Mermaid)
    - Review threat model (STRIDE)
    - Validate against quality checklist

5. **Implement with TDD**:

    ```
    Execute .github/prompts/workflow-spec-to-code.prompt.md for docs/specifications/spec-01-general-user-plant-database.md
    ```

    Outputs:

    - Source files: `src/plants/models.py`, etc.
    - Test files: `tests/test_plants.py`, etc.

6. **Verify Implementation**:

    ```bash
    make lint
    make format
    make test
    /verify src/plants
    /security-review src/plants
    ```

7. **Update Cross-Reference**:

    ```
    /update-docs spec-cross-ref req-01-general-user-plant-database.md
    ```

**Requirement 2: Plant Search & Filter**

Repeat steps 1-7 for:

- `req-02-general-user-plant-search.md`
- `req-03-general-user-plant-filter.md`

---

#### Phase 2: Supporting Calculations & Data

Repeat steps 1-7 for:

- `req-04-general-user-calculations.md`
- `req-05-general-user-usda-zones.md`

---

#### Phase 3: User Experience Enhancements

Repeat steps 1-7 for:

- `req-10-general-user-weather.md`
- `req-11-general-user-notifications.md`
- `req-12-general-user-general-resources.md`

---

#### Phase 4: User Data & Feedback

Repeat steps 1-7 for:

- `req-13-general-user-feedback.md`
- `req-20-general-user-account-favorites.md`
- `req-21-general-user-add-plant.md`

---

#### Phase 5: Advanced General Features

Repeat steps 1-7 for:

- `req-22-general-user-moon-gardening.md`
- `req-06-general-user-pest-database.md`

---

#### Phase 6: Community Features

Repeat steps 1-7 for:

- `req-30-community-member-announcements.md`
- `req-31-community-member-plot-management.md`
- `req-32-community-member-team-chores.md`
- `req-33-community-member-apprentice-program.md`

---

#### Phase 7: Admin Features - DEFERRED

Only proceed after Phases 1-6 complete and deployed:

- `req-40-admin-account-management.md`
- `req-41-admin-educator-role.md`
- `req-42-admin-elevated-access.md`

---

### Automation Opportunities

Consider creating a **meta-workflow script** to automate the repetitive steps:

```bash
# generate-component.sh
#!/bin/bash
COMPONENT_NAME=$1
REQ_FILE="docs/requirements/req-${COMPONENT_NAME}.md"
SPEC_FILE="docs/specifications/spec-${COMPONENT_NAME}.md"

# Step 1: Generate requirement
/create-requirement ${COMPONENT_NAME}

# Step 2: Wait for manual review
echo "Review ${REQ_FILE} and press Enter to continue..."
read

# Step 3: Generate specification + diagrams + threat model
/make-spec-from-req ${REQ_FILE}

# Step 4: Wait for manual review
echo "Review ${SPEC_FILE} and press Enter to continue..."
read

# Step 5: Implement with TDD
/implement-spec ${SPEC_FILE}

# Step 6: Verify
make lint && make format && make test
/verify src/${COMPONENT_NAME}
/security-review src/${COMPONENT_NAME}

# Step 7: Update cross-reference
/update-docs spec-cross-ref ${REQ_FILE}

echo "Component ${COMPONENT_NAME} complete!"
```

---

## Success Criteria

### Requirements Files

Each generated requirement file must:

- [ ] Follow `docs/templates/requirements-template.md` structure exactly
- [ ] Include all template sections (Context, Functional Req, UI/UX, Data, Integration, Constraints, Success Criteria)
- [ ] Map to REQ-000 series (link to specific scope tree section, use cases, performance criteria)
- [ ] Include CodeGuard security considerations in detail
- [ ] Define success criteria with measurable outcomes
- [ ] Include code examples (data models, API interfaces)
- [ ] Define validation rules with error handling
- [ ] Specify accessibility requirements (WCAG 2.1 AA)

### Specifications

Each generated specification must:

- [ ] Be generated from a requirement file via workflow prompt
- [ ] Include three diagram formats (Text, ASCII, Mermaid)
- [ ] Have associated threat model using STRIDE
- [ ] Pass quality review checklist
- [ ] Be tracked in `docs/SPEC-CROSS-REFERENCE.md`

### Implementation

Each implementation must:

- [ ] Follow TDD workflow (Red → Green → Refactor)
- [ ] Pass all tests (unit, integration, end-to-end)
- [ ] Pass linting (`make lint`)
- [ ] Pass formatting (`make format-check`)
- [ ] Pass security review (`/security-review`)
- [ ] Pass verification (`/verify`)
- [ ] Be tracked in `docs/SPEC-CROSS-REFERENCE.md`

### Process Documentation

Update `docs/Process.md` to include:

- [ ] Requirements generation workflow
- [ ] Specification generation workflow
- [ ] Implementation workflow
- [ ] CodeGuard integration process
- [ ] Lessons learned and optimizations
- [ ] Common pitfalls and solutions

---

## Next Steps

### Immediate Actions

1. **Review This Plan**:
   - Validate priority order
   - Adjust scope as needed
   - Confirm timeline expectations

2. **Start with Phase 1, Week 1**:
   - Generate `req-01-general-user-plant-database.md`
   - Execute full workflow (requirement → spec → code)
   - Validate workflow end-to-end
   - Document any adjustments needed

3. **Establish Cadence**:
   - How many requirements per week?
   - Daily standup to track progress?
   - Weekly review of completed components?

### Training Opportunities

As each component completes, update `docs/Process.md` with:

- **What worked well**: Effective prompts, efficient workflow steps
- **What didn't work**: Workflow bottlenecks, template gaps
- **Optimizations**: Automation opportunities, template improvements
- **CodeGuard learnings**: Common security issues, effective mitigations

This will create a **living training document** for the SDD process.

---

## Questions for Clarification

Before proceeding, please confirm:

1. **Priority Order**: Does the proposed priority order match your business objectives?
2. **Timeline**: Are the week estimates reasonable for your availability?
3. **Scope**: Should any components be added, removed, or reordered?
4. **Admin Features**: Confirm these are truly deferred (Phase 7)?
5. **Automation**: Would you like help creating the meta-workflow script?
6. **First Component**: Ready to start with `req-01-general-user-plant-database.md`?

---

**End of Planning Document**

This plan will evolve as we learn and optimize the SDD workflow. All changes should be documented in `docs/Process.md` for future reference and training.
