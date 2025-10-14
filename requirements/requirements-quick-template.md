# Requirements: [ComponentName]

> **Instructions:** Copy this template for each new component. Fill in all sections with as much detail as possible. The more detail you provide here, the better the generated spec will be.

---

## Component Name

**[ComponentName]** - Use PascalCase (e.g., PlantSearch, WeatherWidget, UserProfile)

---

## Context

### Purpose
What problem does this component solve?
-
-
-

### Role in Application
Where does this fit in the overall system?
- Part of which section? (GeneralUser, CommunityGarden, Admin)
- What larger feature does this support?
- How does it connect to other components?

### Target Users
- **Primary Users:** Who will directly use this?
- **Secondary Users:** Who else is affected?
- **User Level:** (Novice gardener, Experienced gardener, Community member, Admin)

### Usage Scenarios
Describe 3-5 concrete scenarios when users will interact with this:
1.
2.
3.
4.
5.

---

## Functional Requirements

### Core Features
List the main features this component MUST have:

1. **[Feature Name]**
   - **Description:** What it does
   - **Behavior:** How it works
   - **User Interaction:** How users engage with it
   - **Example:** Concrete example of use

2. **[Feature Name]**
   - **Description:**
   - **Behavior:**
   - **User Interaction:**
   - **Example:**

3. **[Feature Name]**
   - **Description:**
   - **Behavior:**
   - **User Interaction:**
   - **Example:**

### Business Logic
What rules, calculations, or validations must this component enforce?
-
-
-

### State Management
- **Component owns (internal state):**
  -
  -
- **Receives from parent (props):**
  -
  -
- **Sends to parent (callbacks):**
  -
  -

---

## User Interface Requirements

### Layout Description
Describe the visual structure in plain language:
-
-
-

### Key UI Elements
List all buttons, inputs, displays, etc:
- **[Element Name]:** Purpose, label, behavior
- **[Element Name]:** Purpose, label, behavior
- **[Element Name]:** Purpose, label, behavior

### Responsive Behavior
How does this change on different screen sizes?
- **Desktop (≥1024px):**
- **Tablet (768-1023px):**
- **Mobile (<768px):**

### Visual Style Notes
Any specific colors, fonts, spacing, or style requirements?
-
-
-

### Accessibility Requirements
- [ ] Keyboard navigation support
- [ ] Screen reader compatible
- [ ] ARIA labels for icons/buttons
- [ ] Color contrast meets WCAG AA
- [ ] Focus management
- [ ] Other:

---

## Data Requirements

### Props Interface (TypeScript)
What data does this component receive?

```typescript
interface [ComponentName]Props {
  // Required props
  propName: type;  // Description

  // Optional props
  propName?: type;  // Description

  // Callbacks
  onCallback?: (param: type) => void;  // Description
}
```

### Internal State
What state does the component track internally?
- `[stateName]: type` - Description
- `[stateName]: type` - Description

### API Requirements
Does this component call any APIs?
- **Endpoint:**
- **Method:** GET/POST/PUT/DELETE
- **Request Data:**
- **Response Data:**
- **Error Handling:**

### Data Validation
What validations are needed?
-
-
-

---

## Integration Requirements

### Dependencies
What does this component need?
- **Other Components:** List any child components used
- **Utility Functions:** List helper functions needed
- **React Hooks:** useState, useEffect, custom hooks?
- **External Libraries:** Any third-party packages?

### Parent Component Integration
- **Parent Component:** Name of parent
- **Where it's used:** Which page/section?
- **Props passed from parent:**
- **Callbacks to parent:**

### Child Components
- **Child Component 1:** What props does it receive?
- **Child Component 2:** What props does it receive?

### Page Integration
- **Target Page:** Path to page file (e.g., `src/app/page.tsx`)
- **Import Method:** Static or dynamic import?
- **Section Placement:** Where on the page?
- **Loading Strategy:** SSR, CSR, lazy load?

---

## Constraints

### Technical Stack
- **Backend:** Python Django 4.2+
- **Frontend:** Next.js 15 App Router, React 19
- **Styling:** Tailwind CSS
- **Language:** TypeScript (strict mode)
- **Other:** HTMX, etc.

### Performance Requirements
- **Load Time:** Max acceptable load time
- **Interactivity:** Time to interactive
- **Bundle Size:** Target size limit
- **Rendering:** Frame rate requirements

### File Structure
- **File Location:** `src/components/[ComponentName].tsx`
- **Component Name:** Must match filename (PascalCase)
- **Props Interface:** `[ComponentName]Props`
- **Exports Required:**
  - Default export: component function
  - Named export: props interface
  - Named export: `__isImplemented = true` (for progress tracking)

### Security Considerations
- [ ] Input sanitization needed?
- [ ] Authentication required?
- [ ] Authorization/permissions needed?
- [ ] Sensitive data handling?
- [ ] XSS prevention measures?
- [ ] CSRF protection needed?

### Browser Support
- **Desktop:** Chrome, Firefox, Safari, Edge (last 2 versions)
- **Mobile:** iOS Safari 14+, Android Chrome 90+
- **Accessibility:** WCAG 2.1 Level AA

---

## Success Criteria

### Functional Checklist
- [ ] All core features work as described
- [ ] Business logic is correct
- [ ] State management works properly
- [ ] Error handling covers edge cases
- [ ] Data validation works correctly

### UI/UX Checklist
- [ ] Layout matches description
- [ ] Responsive at all breakpoints
- [ ] Interactive elements provide feedback
- [ ] Accessibility requirements met
- [ ] Loading states display correctly

### Integration Checklist
- [ ] Integrates with parent component
- [ ] Props are correctly typed
- [ ] Callbacks work as expected
- [ ] Child components receive correct data
- [ ] Page integration is seamless

### Technical Checklist
- [ ] TypeScript type-check passes
- [ ] File in correct location with correct name
- [ ] Props interface follows naming convention
- [ ] Exports `__isImplemented = true` marker
- [ ] No console errors or warnings
- [ ] Performance requirements met

### Testing Checklist
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing
- [ ] Edge cases covered
- [ ] Accessibility tested with screen reader
- [ ] Cross-browser testing completed

---

## Additional Notes

### Open Questions
List any unresolved questions or decisions needed:
-
-
-

### Future Enhancements
Features for later iterations:
-
-
-

### Related Specifications
Link to related components or features:
-
-
-

### Reference Materials
Any mockups, designs, or documentation to reference?
-
-
-

---

## Quick Checklist Before Generating Spec

- [ ] Component name is clear and follows naming conventions
- [ ] Context section explains the "why" (purpose and value)
- [ ] All core features are listed with descriptions
- [ ] UI layout is clearly described
- [ ] Props interface is complete with types
- [ ] Integration points are identified
- [ ] Success criteria are specific and testable
- [ ] All sections are filled out (no empty sections)

---

**Next Step:** Run `/make-spec-from-req [ComponentName] [this-file.md]` to generate the specification document.
