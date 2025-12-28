---
title: Requirements Files to Generate for GenAI Created MVP
description: GenAI suggested requirements files to generate. Still needs to be reviewed as of 20251227 for alignment with original MVP plans. It also seems to be for more than just an MVP.
---

## [Requirements Files to Generate](./MVP_Reqs_By_GenAI.md)

### Phase 1: Core Plant Database (3 files)

#### 1. `req-general-user-plant-database.md`

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

#### 2. `req-general-user-plant-search.md`

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

#### 3. `req-general-user-plant-filter.md`

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

#### 4. `req-general-user-calculations.md`

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

#### 5. `req-general-user-usda-zones.md`

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

#### 6. `req-general-user-weather.md`

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

#### 7. `req-general-user-notifications.md`

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

#### 8. `req-general-user-general-resources.md`

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

#### 9. `req-general-user-feedback.md`

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

#### 10. `req-general-user-account-favorites.md`

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

#### 11. `req-general-user-add-plant.md`

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

#### 12. `req-general-user-moon-gardening.md`

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

#### 13. `req-general-user-pest-database.md`

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

#### 14. `req-community-member-announcements.md`

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

#### 15. `req-community-member-plot-management.md`

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

#### 16. `req-community-member-team-chores.md`

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

#### 17. `req-community-member-apprentice-program.md`

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

#### 18. `req-admin-account-management.md`

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

#### 19. `req-admin-educator-role.md`

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

#### 20. `req-admin-elevated-access.md`

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
