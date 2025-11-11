# Spec Template for Gardening Application

Copy this template for all workshop exercises:

## Feature: [Component/Feature Name]

### Context
- Purpose and role in the application
- How it fits into the larger system
- Who will use it and when

### Requirements
- Functional requirements (what it must do)
- User interface requirements
- Data requirements
- Integration requirements
  - Component imports and dependencies
  - Data flow and prop passing
  - Parent component integration
  - Page integration (where applicable)
    - File to modify (e.g., `src/app/page.tsx`)
    - Dynamic import configuration
    - Wrapper component with error handling
    - Section placement and positioning
    - Props and callbacks to provide
    - Component progress indicator updates
      - Each component will have a placeholder that will update when the component is implemented
      - Add dynamic import at top of page.tsx (if new component)
      - Update progress indicator section with dynamic detection logic
      - Use conditional rendering: `{componentStatus.yourComponent ? '✅' : '⏳'}`

### Constraints
- Technical stack and frameworks (Python, Django, HTMX, Next.js 15, React 19, TypeScript, Tailwind CSS)
- Performance requirements (load times, rendering thresholds)
- Design constraints (responsive breakpoints, component size limits)
- File structure and naming conventions
  - **CRITICAL:** Component file name MUST match the name used in page.tsx dynamic imports
  - File location: `src/components/[ComponentName].tsx` (PascalCase)
  - Component name: `[ComponentName]` (same as filename without extension)
  - Example: `src/components/CustomerCard.tsx` → `import('@/components/CustomerCard')`
  - **For progress tracking to work:** Ensure component name matches detection logic in page.tsx
- Props interface and TypeScript definitions
- Security considerations
- **CRITICAL: Automatic Placeholder Detection**
  - System auto-detects placeholders vs real implementations
  - Detection method: Checks for **`__isImplemented` marker**
  - Placeholders: Only have `export default` (no marker)
  - Real implementations: MUST export implementation marker
  - Example of real implementation that triggers auto-detection:
    ```typescript
    export interface ComponentNameProps {
      prop1: string;
      prop2?: number;
    }

    export default function ComponentName(props: ComponentNameProps) {
      // Real implementation with full UI
    }

    // REQUIRED: Add this marker at the end!
    export const __isImplemented = true;
    ```
  - **REQUIRED**: Add `export const __isImplemented = true;` to all real implementations
  - This marker exists at runtime (unlike TypeScript interfaces) for detection

### Acceptance Criteria
- [ ] Testable success criteria
- [ ] Edge cases handled
- [ ] User experience validated
- [ ] Integration points verified
- [ ] Component implemented and saved to correct file location
- [ ] Component visible and functional on dashboard page
- [ ] Error handling and loading states working correctly
- [ ] Workshop progress indicators updated with dynamic detection
  - [ ] Component added to `componentStatus` state in page.tsx
  - [ ] Progress indicator uses conditional rendering based on component detection
  - [ ] Indicator automatically updates when component is implemented
- [ ] TypeScript type-check passes (npm run type-check)
- [ ] No console errors when component loads
- [ ] **Auto-detection requirements:**
  - [ ] Component exports `__isImplemented = true` marker at the end of file
  - [ ] Component exports a TypeScript Props interface for type safety
  - [ ] Props interface follows naming convention: `[ComponentName]Props`
  - [ ] Progress tracking automatically detects implementation via marker
  - [ ] Dashboard shows ✅ for implemented component after page refresh