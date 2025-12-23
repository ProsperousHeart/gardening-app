# Requirements: PlantSearch Component

This is an example requirements document showing how to use the requirements template for a concrete component in the gardening application.

---

## Component Name

**PlantSearch**

---

## Context

### Purpose
- Enables gardeners to discover plants suitable for their growing conditions
- Provides powerful filtering capabilities to narrow down plant database
- Allows users to find plants by various characteristics (zone, type, sun exposure, special attributes)

### Role in Application
- Central feature of the GeneralUser section
- Primary entry point for plant discovery workflow
- Feeds into plant detail views and user favorites/collections
- Supports the core use case: "What can I grow in my garden?"

### Users
- **Primary Users:** All gardeners (novice to expert) seeking plant recommendations
- **Secondary Users:** Community garden members researching plants for shared spaces

### Usage Scenarios
- First-time user wants to find perennials that grow in zone 6b
- Experienced gardener searches for drought-tolerant plants for dry area
- Community garden member finds pollinator-friendly plants for shared space
- User browses favorites and wants to filter by planting season
- Gardener searches for companion plants for tomatoes

---

## Functional Requirements

### Core Features

1. **Search by Plant Name**
   - Description: Free-text search that matches common or scientific plant names
   - Behavior: Real-time filtering as user types, case-insensitive, partial match support
   - User interaction: Text input with clear button, displays match count

2. **Filter by Hardiness Zone**
   - Description: Filter plants by USDA hardiness zones (1a-13b)
   - Behavior: Shows only plants that can survive in selected zone
   - User interaction: Dropdown or zone selector, allows "my zone" quick select

3. **Filter by Plant Type**
   - Description: Filter by plant category (Annual, Perennial, Biennial, Shrub, Tree, Vine)
   - Behavior: Multi-select filter, shows plants matching any selected type
   - User interaction: Checkbox group or multi-select dropdown

4. **Filter by Sun Exposure**
   - Description: Filter by light requirements (Full Sun, Partial Sun, Partial Shade, Shade)
   - Behavior: Multi-select filter, matches plants with compatible exposure
   - User interaction: Icon-based selector or checkbox group

5. **Filter by Special Characteristics**
   - Description: Filter by attributes (drought tolerant, deer resistant, pollinator friendly, native, edible, medicinal)
   - Behavior: Multi-select filter with AND logic (must have all selected attributes)
   - User interaction: Toggle chips or checkbox group with icons

6. **Clear Filters**
   - Description: Reset all filters to default state
   - Behavior: Clears all selections and shows full plant database
   - User interaction: Clear button visible when filters are active

7. **Results Count & Feedback**
   - Description: Display count of plants matching current filters
   - Behavior: Updates in real-time as filters change
   - User interaction: Prominent display above results, empty state message when no matches

### Business Logic
- Zone filtering uses plant minimum hardiness zone (plant must tolerate or be hardy to colder zones)
- Multiple characteristics use AND logic (plant must have ALL selected characteristics)
- Multiple types use OR logic (plant can be ANY selected type)
- Search matches against both common and scientific names
- Default view shows plants for user's saved zone preference (if set)

### State Management
- **Local State:**
  - Search query text
  - Selected hardiness zone
  - Selected plant types (array)
  - Selected sun exposures (array)
  - Selected characteristics (array)
  - Filtered results (computed from all filters)
  - Active filters count (for badge display)

- **Parent State (received via props):**
  - Full plant database array
  - User's preferred hardiness zone (from user settings)
  - User's favorite plants (for marking favorites in results)

- **Parent Communication (via callbacks):**
  - onPlantSelect: When user clicks a plant to view details
  - onFavoriteToggle: When user favorites/unfavorites a plant
  - onFilterChange: When filters change (for analytics)

---

## User Interface Requirements

### Layout & Structure
- **Search Bar Section** (top): Full-width search input with icon and clear button
- **Filters Section** (below search): Horizontal filter chips/buttons that wrap responsively
- **Results Count** (above results): Shows "X plants found" or "No plants match your filters"
- **Results Grid** (main area): Responsive grid of plant cards (see PlantCard component)
- **Mobile:** Filters collapse into expandable drawer or accordion

### Visual Design
- **Color Scheme:**
  - Primary: Green (#10b981) for active filters and primary actions
  - Secondary: Gray (#6b7280) for inactive filters
  - Background: White (#ffffff) for cards, light gray (#f9fafb) for page
  - Accent: Blue (#3b82f6) for interactive elements

- **Typography:**
  - Search input: text-base (16px)
  - Filter labels: text-sm (14px)
  - Results count: text-lg font-semibold (18px)
  - Empty state: text-base text-gray-600

- **Spacing:**
  - Component padding: p-4 (16px)
  - Filter spacing: gap-2 (8px between filters)
  - Search bar margin bottom: mb-4 (16px)
  - Results grid gap: gap-4 (16px)

- **Borders & Shadows:**
  - Search input: border rounded-lg, focus ring
  - Filter chips: rounded-full, border when inactive
  - Cards: shadow-sm hover:shadow-md transition

### Interactive Elements
- **Search Input:**
  - Label: "Search plants by name"
  - Placeholder: "Search for plants..."
  - Clear button (X icon) appears when text entered
  - Search icon on left side

- **Filter Chips:**
  - Inactive: white background, gray border, gray text
  - Active: green background, white text, no border
  - Hover: slight scale transform (scale-105)
  - Badge showing count of active filters

- **Clear All Button:**
  - Only visible when filters are active
  - Label: "Clear all filters"
  - Red text color for visibility
  - Positioned at end of filter row

- **Results Grid:**
  - Responsive columns: 1 col mobile, 2 cols tablet, 3-4 cols desktop
  - Each plant card is clickable
  - Favorite icon toggles on each card
  - Loading skeleton while data loads

### Responsive Behavior
- **Desktop (>= 1024px):**
  - Search bar max-width: 600px, centered
  - Filters display as horizontal row with wrapping
  - Results grid: 4 columns
  - Filters always visible

- **Tablet (768px - 1023px):**
  - Search bar full width with side padding
  - Filters display as horizontal row with wrapping
  - Results grid: 2 columns
  - Filters always visible

- **Mobile (< 768px):**
  - Search bar full width
  - Filters collapse into "Filters" button that opens drawer/sheet
  - Badge on filter button shows active filter count
  - Results grid: 1 column
  - Sticky search bar at top

### Accessibility Requirements
- Search input has proper label (can be visually hidden)
- Filter controls are keyboard navigable (Tab, Enter, Space)
- ARIA labels for icon-only buttons ("Clear search", "Toggle filters")
- ARIA live region announces results count changes
- Focus management: focus returns to trigger when closing filter drawer
- Color contrast meets WCAG AA standards (4.5:1 for text)
- Screen reader announces "X plants found" when filters change

---

## Data Requirements

### Props Interface

```typescript
interface PlantSearchProps {
  // Plant database
  plants: Plant[];  // Full array of plant objects

  // User preferences
  userZone?: string;  // User's saved hardiness zone (e.g., "6b")
  favoritePlantIds?: string[];  // Array of plant IDs user has favorited

  // Callbacks
  onPlantSelect: (plantId: string) => void;  // When user clicks a plant card
  onFavoriteToggle?: (plantId: string) => void;  // When user toggles favorite
  onFilterChange?: (filters: FilterState) => void;  // When filters change (for analytics)

  // Optional customization
  initialFilters?: FilterState;  // Pre-populate filters (e.g., from URL params)
  resultsPerPage?: number;  // Number of results to show (default: show all)
}

// Supporting type definitions
interface Plant {
  id: string;
  commonName: string;
  scientificName: string;
  hardinessZoneMin: string;  // e.g., "6a"
  hardinessZoneMax: string;  // e.g., "9b"
  plantType: PlantType;
  sunExposure: SunExposure[];  // Array because plant may tolerate multiple
  isDroughtTolerant: boolean;
  isDeerResistant: boolean;
  isPollinatorFriendly: boolean;
  isNative: boolean;
  isEdible: boolean;
  isMedicinal: boolean;
  // ... other plant properties
}

type PlantType = 'Annual' | 'Perennial' | 'Biennial' | 'Shrub' | 'Tree' | 'Vine';
type SunExposure = 'Full Sun' | 'Partial Sun' | 'Partial Shade' | 'Shade';

interface FilterState {
  searchQuery: string;
  selectedZone: string | null;
  selectedTypes: PlantType[];
  selectedExposures: SunExposure[];
  selectedCharacteristics: string[];  // Array of characteristic keys
}
```

### Internal State

```typescript
// Filter state
const [searchQuery, setSearchQuery] = useState<string>('');
const [selectedZone, setSelectedZone] = useState<string | null>(userZone || null);
const [selectedTypes, setSelectedTypes] = useState<PlantType[]>([]);
const [selectedExposures, setSelectedExposures] = useState<SunExposure[]>([]);
const [selectedCharacteristics, setSelectedCharacteristics] = useState<string[]>([]);

// UI state
const [isFilterDrawerOpen, setIsFilterDrawerOpen] = useState<boolean>(false);  // Mobile only

// Computed state (useMemo)
const filteredPlants = useMemo(() => {
  // Filter logic here
}, [plants, searchQuery, selectedZone, selectedTypes, selectedExposures, selectedCharacteristics]);

const activeFilterCount = useMemo(() => {
  // Count active filters
}, [selectedZone, selectedTypes, selectedExposures, selectedCharacteristics]);
```

### API Requirements
- **No direct API calls from this component**
- Plant data is passed via props from parent component
- Parent component handles fetching plant database from API

### Data Validation
- Search query is trimmed and sanitized (no special regex characters)
- Zone values must match valid USDA zone format (1a-13b)
- Plant type selections must match PlantType enum
- Exposure selections must match SunExposure enum
- Characteristic selections validated against known characteristics list

---

## Integration Requirements

### Component Dependencies
- **React/Next.js Components:**
  - `next/dynamic` for lazy loading PlantCard (if results are large)
  - Custom `PlantCard` component (see PlantCard spec)
  - Custom `FilterChip` component (reusable filter button)
  - Custom `SearchInput` component (optional, or use native input)

- **UI Library Components (if using shadcn/ui or similar):**
  - `Sheet` component for mobile filter drawer
  - `Badge` component for active filter count
  - `Button` component for filter chips

- **Utility Functions:**
  - `filterPlantsByZone(plants, zone)` - Zone filtering logic
  - `filterPlantsBySearch(plants, query)` - Search matching logic
  - `compareZones(zone1, zone2)` - Compare hardiness zones

- **Hooks:**
  - `useState` for filter state
  - `useMemo` for computed filtered results
  - `useEffect` for calling onFilterChange callback
  - `useCallback` for memoized event handlers
  - Custom `useDebounce` hook for search input (optional)

- **External Libraries:**
  - None required (all functionality can be built with React)
  - Optional: `fuse.js` for fuzzy search if desired

### Parent Component Integration
- **Parent Component:** `PlantDatabasePage` or similar dashboard page
- **Prop Passing:**
  - Parent fetches full plant database from API/database
  - Parent provides user's zone preference from user settings/context
  - Parent provides favorite plant IDs from user profile
- **Callback Functions:**
  - `onPlantSelect`: Parent navigates to plant detail page or opens modal
  - `onFavoriteToggle`: Parent updates user's favorites in database
  - `onFilterChange`: Parent logs analytics event (optional)

### Child Components
- **Subcomponents:**
  - `PlantCard` - Displays individual plant in results grid
  - `FilterChip` - Reusable filter button/toggle
  - `SearchInput` - Search bar with clear button (optional, can use native)
  - `EmptyState` - Message when no results found

- **Data Flow to Children:**
  - `PlantCard` receives: `plant` object, `isFavorite` boolean, `onSelect`, `onFavoriteToggle`
  - `FilterChip` receives: `label`, `isActive`, `onClick`, `icon` (optional)
  - `EmptyState` receives: `message`, `action` (optional clear filters button)

### Page Integration
- **Target Page:** `src/app/page.tsx` (main dashboard) or `src/app/plants/page.tsx`
- **File Location:** Component saved to `src/components/PlantSearch.tsx`
- **Import Method:** Dynamic import for better performance
  ```typescript
  const PlantSearch = dynamic(() => import('@/components/PlantSearch'), {
    loading: () => <PlantSearchSkeleton />,
    ssr: true  // Enable SSR for SEO
  });
  ```
- **Error Boundary:** Yes, wrap in error boundary to prevent full page crash
- **Section Placement:** Primary section on plant database page, above fold
- **Loading Strategy:** SSR enabled for initial render, then client-side interactivity

### Progress Tracking Integration
- **Dynamic Import:** Yes, using `next/dynamic`
- **Progress Indicator:** Yes, should appear in workshop progress dashboard
- **Detection Logic:** Component exports `__isImplemented = true` at end of file
- **Page.tsx Updates:**
  ```typescript
  // Add to page.tsx dynamic imports
  const PlantSearch = dynamic(() => import('@/components/PlantSearch'));

  // Add to componentStatus state
  const [componentStatus, setComponentStatus] = useState({
    plantSearch: false,  // Auto-detected
    // ... other components
  });

  // Progress indicator will show: {componentStatus.plantSearch ? '✅' : '⏳'}
  ```

---

## Constraints

### Technical Stack
- **Backend:** Python Django 4.2+, Django REST Framework for API
- **Frontend:** Next.js 15 App Router, React 19
- **Styling:** Tailwind CSS 3.x
- **Language:** TypeScript 5.x (strict mode enabled)
- **Build:** Turbopack for development, Webpack for production

### Performance Requirements
- **Initial Load Time:** < 1 second for component render (with 1000 plants)
- **Time to Interactive:** < 500ms after initial render
- **Search Responsiveness:** < 100ms debounced search filtering
- **Bundle Size:** < 50KB gzipped (including dependencies)
- **Rendering Performance:** Maintain 60fps during filter interactions
- **Large Data Handling:** Efficiently filter up to 5000+ plants without lag

### Design Constraints
- **Responsive Breakpoints:**
  - Mobile: < 768px (1 column grid, drawer filters)
  - Tablet: 768px - 1023px (2 column grid, inline filters)
  - Desktop: >= 1024px (4 column grid, inline filters)

- **Component Max Width:** 1400px (centered on ultra-wide screens)
- **Card Grid Gap:** 16px (gap-4) between cards
- **Spacing System:** Tailwind's default spacing scale (4px base unit)
- **Color Palette:**
  - Primary green: tailwind green-500
  - Gray scale: tailwind gray palette
  - Error: tailwind red-500
  - Info: tailwind blue-500

### File Structure & Naming Conventions
- **File Location:** `src/components/PlantSearch.tsx`
- **Component Name:** `PlantSearch` (matches filename)
- **Props Interface Name:** `PlantSearchProps`
- **File Exports:**
  ```typescript
  // Default export: component
  export default function PlantSearch(props: PlantSearchProps) { ... }

  // Named exports: types and implementation marker
  export type { PlantSearchProps, FilterState };
  export const __isImplemented = true;
  ```

### Security Considerations
- **Input Sanitization:**
  - Search query sanitized to prevent regex injection
  - All user input escaped before rendering
  - No innerHTML or dangerouslySetInnerHTML usage

- **Authentication:** Not required for viewing plants (public data)
- **Authorization:** Favorite toggle requires authenticated user
- **Data Privacy:** No PII collected or displayed in this component
- **XSS Prevention:**
  - All user input escaped
  - Use React's built-in XSS protection
  - Validate all props at runtime (TypeScript + runtime checks)

- **CSRF Protection:** Handled at API level by Django (not component concern)

### Browser & Device Support
- **Browsers:**
  - Chrome 90+ (last 2 versions)
  - Firefox 88+ (last 2 versions)
  - Safari 14+ (last 2 versions)
  - Edge 90+ (last 2 versions)

- **Mobile Devices:**
  - iOS Safari 14+ (iPhone 6s and newer)
  - Android Chrome 90+ (Android 8+)

- **Accessibility Standards:** WCAG 2.1 Level AA compliance required

---

## Success Criteria

### Functional Validation
- [ ] Search filters plants by common and scientific name (case-insensitive, partial match)
- [ ] Zone filter shows only plants hardy to selected zone or colder
- [ ] Type filter works with multiple selections (OR logic)
- [ ] Exposure filter works with multiple selections (OR logic)
- [ ] Characteristic filter works with multiple selections (AND logic)
- [ ] Clear filters button resets all filters and shows full database
- [ ] Results count updates in real-time as filters change
- [ ] Empty state displays when no plants match filters
- [ ] User's preferred zone pre-populates zone filter (if set)
- [ ] Clicking plant card calls onPlantSelect with correct plant ID
- [ ] Toggling favorite calls onFavoriteToggle with correct plant ID

### UI/UX Validation
- [ ] Layout matches design specifications
- [ ] Component is fully responsive at all breakpoints
- [ ] Filter drawer opens/closes smoothly on mobile
- [ ] Search input provides immediate visual feedback
- [ ] Active filters are visually distinct from inactive filters
- [ ] Loading skeleton displays while initial data loads
- [ ] Hover states work on all interactive elements
- [ ] Transitions are smooth (no janky animations)
- [ ] Empty state is clear and helpful
- [ ] Active filter count badge displays correctly

### Integration Validation
- [ ] Component receives plants array prop and renders correctly
- [ ] Component receives userZone and pre-populates filter
- [ ] Component receives favoritePlantIds and marks cards correctly
- [ ] onPlantSelect callback fires with correct plant ID
- [ ] onFavoriteToggle callback fires with correct plant ID
- [ ] onFilterChange callback fires when filters change (if provided)
- [ ] PlantCard child components receive correct props
- [ ] Component integrates seamlessly into parent page

### Technical Validation
- [ ] TypeScript type-check passes with zero errors (`npm run type-check`)
- [ ] Component file is at `src/components/PlantSearch.tsx`
- [ ] Props interface named `PlantSearchProps`
- [ ] Component exports `__isImplemented = true` marker
- [ ] No console errors or warnings in development or production
- [ ] Bundle size is under 50KB gzipped
- [ ] Filtering 1000 plants takes < 100ms
- [ ] Component maintains 60fps during interactions
- [ ] ESLint passes with no errors or warnings

### Testing Validation
- [ ] Unit tests written for filtering logic (zone, type, exposure, characteristics)
- [ ] Unit tests written for search matching logic
- [ ] Unit tests verify callback functions are called correctly
- [ ] Integration test verifies component renders with mock data
- [ ] Integration test verifies filtering updates results correctly
- [ ] Edge case tests: empty database, no matches, all filters active
- [ ] Accessibility tested with keyboard navigation (Tab, Enter, Escape)
- [ ] Accessibility tested with VoiceOver (Mac) or NVDA (Windows)
- [ ] Cross-browser testing completed (Chrome, Firefox, Safari, Edge)
- [ ] Mobile device testing completed (iOS Safari, Android Chrome)

---

## Notes & Considerations

### Open Questions
- Should we implement pagination or infinite scroll for large result sets?
- Do we want to save filter state to URL query params for shareable links?
- Should we add a "sort by" feature (alphabetical, zone, type)?
- Do we want to track filter usage analytics to understand user behavior?

### Future Enhancements
- **Advanced Search:** Search by additional attributes (height, spacing, bloom time)
- **Saved Searches:** Allow users to save favorite filter combinations
- **Comparison Mode:** Select multiple plants to compare side-by-side
- **AI Recommendations:** "Plants similar to this one" suggestions
- **Map View:** Show plants on hardiness zone map
- **Seasonal Filtering:** Filter by planting season or bloom time

### Related Specifications
- `PlantCard` spec - Displays individual plant in results
- `PlantDetailPage` spec - Full plant information page (onPlantSelect destination)
- `UserSettings` spec - Source of user's preferred hardiness zone
- `FavoritesManager` spec - Manages user's favorite plants collection
