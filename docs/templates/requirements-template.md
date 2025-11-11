# Requirements Template

Use this template when creating requirements documents for new features or modules. This structured format ensures all necessary information is captured for generating comprehensive specifications.

---

## Feature/Module Name

**[FeatureName]** - Use descriptive naming (e.g., snake_case for Python modules, descriptive names for features)

---

## Context

### Purpose

- What problem does this feature/module solve?
- What value does it provide to users?
- Why is this needed?

### Role in Application

- Where does this fit in the overall system architecture?
- What larger feature or user story does this support?
- How does it interact with existing components?

### Users

- **Primary Users:** Who will directly interact with this feature?
- **Secondary Users:** Who else might be affected by this feature?
- **Stakeholders:** Who has interest in this feature?

### Usage Scenarios

- When will users interact with this feature?
- What triggers its execution or activation?
- What are common user workflows involving this feature?

---

## Functional Requirements

### Core Features

List the essential functionality this feature must provide:

1. **[Feature 1 Name]**

   - Description: What it does
   - Behavior: How it behaves
   - User interaction: How users engage with it
   - Expected input and output

2. **[Feature 2 Name]**
   - Description: What it does
   - Behavior: How it behaves
   - User interaction: How users engage with it
   - Expected input and output

### Business Logic

- What calculations, validations, or processing must occur?
- What business rules govern this feature's behavior?
- What data transformations are required?
- What algorithms or logic patterns are needed?

### State Management

- What state does this feature manage?
- What configuration is required?
- What persistent data needs to be maintained?
- How is state synchronized across the system?

---

## Interface Requirements

### Layout & Structure

- Component dimensions (fixed, flexible, responsive)
- Major UI sections and their arrangement
- Visual hierarchy and organization

### Visual Design

- Color scheme (primary, secondary, accent colors)
- Typography (headings, body text, labels)
- Spacing and padding requirements
- Border and shadow treatments

### Interactive Elements

- Buttons (labels, types, actions)
- Form inputs (types, labels, validation messages)
- Links and navigation elements
- Interactive feedback (hover states, active states, disabled states)

### Responsive Behavior

- Desktop layout (>= 1024px)
- Tablet layout (768px - 1023px)
- Mobile layout (< 768px)
- Breakpoint-specific changes

### Accessibility Requirements

- Keyboard navigation support
- Screen reader compatibility
- ARIA labels and roles
- Focus management
- Color contrast requirements

### Module/Package Interface (for Python code)

Define the public API:

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what the function does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: Description of when this is raised
    """
    pass
```

### Command-Line Interface (if applicable)

- Command structure and syntax
- Arguments and options (required vs optional)
- Input/output format
- Exit codes and their meanings
- Help text and documentation

### API Endpoints (if applicable)

- Endpoint paths and HTTP methods
- Request/response formats (JSON, XML, etc.)
- Authentication requirements
- Rate limiting and quotas
- Error response formats

### User Interface (if applicable)

- UI components and layout
- User interactions and workflows
- Visual design requirements
- Accessibility requirements

---

## Data Requirements

### Data Models and Schemas

Define the data structures used:

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelName:
    """Brief description of the data model."""
    field1: str  # Description
    field2: int  # Description
    field3: Optional[str] = None  # Description
```

Or for database models:

```python
# SQLAlchemy example
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelName(Base):
    __tablename__ = 'table_name'

    id = Column(Integer, primary_key=True)
    field1 = Column(String(100), nullable=False)
    field2 = Column(Integer, nullable=False)
```

### Input/Output Specifications

- Expected input formats (JSON, CSV, binary, etc.)
- Output formats and structure
- Data validation rules
- File formats and encodings
- Data size limits

### Storage Requirements

- Database tables/collections needed
- File storage requirements
- Caching strategy
- Data retention and lifecycle policies
- Backup and recovery requirements

### API Requirements

- **Endpoints:** What API endpoints does this component consume?
- **Request Format:** What data is sent to the API?
- **Response Format:** What data structure is returned?
- **Error Handling:** How should API errors be handled?

### Data Validation

- Input validation rules
- Data type constraints
- Business rule validations
- Data format requirements
- Error messages for validation failures
- Handling of invalid data

---

## Integration Requirements - UI Front End

### Component Dependencies

- **React/Next.js Components:** What built-in or third-party components are needed?
- **Utility Functions:** What helper functions or utilities are required?
- **Hooks:** What React hooks (built-in or custom) will be used?
- **External Libraries:** What third-party libraries are needed?

### Parent Component Integration

- **Parent Component:** What component will render this component?
- **Prop Passing:** What data flows from parent to this component?
- **Callback Functions:** What events/data need to be communicated back to parent?

### Child Components

- **Subcomponents:** What child components will this component render?
- **Data Flow to Children:** What props will be passed to child components?

### Page Integration (if applicable)

- **Target Page:** Which page(s) will include this component?
- **File Location:** Path to the page file (e.g., `src/app/page.tsx`)
- **Import Method:** Static import or dynamic import?
- **Error Boundary:** Does this need to be wrapped in error boundary?
- **Section Placement:** Where on the page should this component appear?
- **Loading Strategy:** Lazy loading, suspense boundaries, or immediate load?

### Progress Tracking Integration

- **Dynamic Import:** Will this use dynamic import for lazy loading?
- **Progress Indicator:** Should this component's status appear in workshop progress tracking?
- **Detection Logic:** What marker will indicate component is implemented?

---

## Integration Requirements (Python Specific)

### Module Dependencies

- **Standard Library:** What built-in modules are needed?
- **Third-Party Packages:** What external packages are required?
  - Package name and version constraints
  - Purpose of each dependency
  - License compatibility
- **Internal Modules:** What other project modules are needed?

### External Service Integrations

- APIs, databases, message queues, etc.
- Authentication and authorization requirements
- Connection management and pooling
- Retry logic and circuit breakers
- Timeout and error handling

### Data Flow

- How data flows between components
- Event handling and callbacks
- Message passing or queue integration
- Signal/slot patterns (if applicable)
- Synchronous vs asynchronous processing

### Configuration Requirements

- Environment variables
- Configuration files and formats (JSON, YAML, INI, etc.)
- Runtime configuration options
- Configuration validation
- Secrets management

---

## Constraints

### Technical Stack

- **Language:** Python version (e.g., Python 3.12+)
- **Backend Framework:** Django, Flask, FastAPI, etc. (with versions)
- **Database:** PostgreSQL, MySQL, SQLite, MongoDB, etc.
- **Frontend:** (if applicable) React, Vue, HTMX, etc.
- **Styling:** Tailwind CSS
- **Other Technologies:** Message queues, caching, search engines, etc.

### Performance Requirements

#### Frontend Performance

- **Initial Load Time:** Maximum acceptable load time
- **Time to Interactive:** When should component become interactive?
- **Bundle Size:** Maximum JavaScript bundle size
- **Rendering Performance:** Frame rate requirements, large list handling

#### Backend Performance

- **Response Time:** Maximum acceptable response time
- **Throughput:** Requests/transactions per second
- **Resource Limits:** Memory, CPU, disk usage constraints
- **Scalability:** Horizontal vs vertical scaling requirements
- **Concurrency:** Number of concurrent operations supported

### Design Constraints

#### Frontend Design Constraints

- **Responsive Breakpoints:**
  - Mobile: < 768px
  - Tablet: 768px - 1023px
  - Desktop: >= 1024px
- **Component Size Limits:** Max width, max height
- **Spacing System:** Tailwind spacing scale to use
- **Color Palette:** Allowed colors from design system

#### Backend Design Constraints

- **Code Structure:**
  - Module organization (`src/`, `tests/`, etc.)
  - Package naming conventions (lowercase with underscores)
  - File naming conventions (snake_case for Python files)
- **Coding Standards:**
  - PEP 8 compliance
  - Black formatting (88 character line length)
  - flake8 linting rules
  - Type hints and mypy compliance
- **Documentation:**
  - Docstring format (Google, NumPy, or reStructuredText)
  - ABOUTME comments at top of files
  - README and user documentation
- **Testing:**
  - Test file naming (`test_*.py`)
  - Test coverage minimums
  - pytest conventions
- **Logging:**
  - Use of project logger utility
  - Log levels and formatting
  - Decorator usage (if applicable)

### File Structure & Naming Conventions

- **Module Location:** `src/[module_name]/`
- **Test Location:** `tests/test_[module_name].py`
- **File Naming:** snake_case for Python files
- **Class Naming:** PascalCase for classes
- **Function Naming:** snake_case for functions
- **Constants:** UPPER_CASE for constants

### Security Considerations

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

### Browser & Device Support

- **Browsers:** Chrome, Firefox, Safari, Edge (versions)
- **Mobile Devices:** iOS Safari, Android Chrome
- **Accessibility Standards:** WCAG 2.1 Level AA compliance

### Platform & Environment

- **Operating Systems:** Linux, macOS, Windows support
- **Python Version:** Minimum version required
- **Virtual Environment:** uv/uvx setup (see [uvx setup guide](../uvx-setup-guide.md))
- **Deployment Environment:** Docker, Kubernetes, bare metal, cloud platform
- **Environment Variables:** Required environment configuration

---

## Success Criteria

### Functional Validation

- [ ] All core features work as specified
- [ ] Business logic produces correct results
- [ ] State management functions properly
- [ ] Error handling works for all edge cases
- [ ] Input validation catches invalid data
- [ ] Output format matches specifications

### UI/UX Validation

- [ ] Layout matches design specifications
- [ ] Component is responsive at all breakpoints
- [ ] Interactive elements provide appropriate feedback
- [ ] Accessibility requirements are met
- [ ] Loading states display appropriately

### Integration Validation

- [ ] Module integrates correctly with other components
- [ ] External service integrations work correctly
- [ ] Data flow operates as expected
- [ ] Configuration loads and validates properly
- [ ] Dependencies are properly declared
- [ ] Page integration is seamless (if applicable)

### Performance Validation

- [ ] Response times meet requirements
- [ ] Throughput meets requirements
- [ ] Resource usage within limits
- [ ] Handles expected load without degradation
- [ ] Scales as designed

### Technical Validation

#### Frontend Technical Validation

- [ ] TypeScript type-check passes with no errors
- [ ] Component file is in correct location with correct name
- [ ] Props interface follows naming convention
- [ ] Component exports `__isImplemented = true` marker
- [ ] No console errors or warnings
- [ ] Performance requirements are met

#### Backend Technical Validation

- [ ] Code follows project style guidelines (PEP 8, Black, flake8)
- [ ] Type hints are complete and correct (if using mypy)
- [ ] Module is in correct location with correct naming
- [ ] ABOUTME comments present at top of files
- [ ] No linting errors or warnings
- [ ] Logging implemented correctly

### Testing Validation

- [ ] Unit tests written and passing
- [ ] Integration tests written and passing
- [ ] Acceptance tests written and passing
- [ ] Edge cases covered by tests
- [ ] Test coverage meets project standards (e.g., 80%+)
- [ ] Tests use proper isolation (e.g., mocking, test fixtures)
- [ ] Tests are readable and maintainable
- [ ] Accessibility tested with screen reader
- [ ] Cross-browser testing completed

### Security Validation

- [ ] Security requirements met
- [ ] Input validation and sanitization implemented
- [ ] Authentication/authorization working correctly
- [ ] No security vulnerabilities introduced
- [ ] Sensitive data properly protected
- [ ] Security scanning passes (e.g., bandit, safety)

### Documentation Validation

- [ ] Code documentation complete (docstrings)
- [ ] API documentation updated (if applicable)
- [ ] User documentation updated (if applicable)
- [ ] Configuration documented
- [ ] README updated with new feature information

### Deployment Validation

- [ ] Feature works in target environment(s)
- [ ] Dependencies installed correctly
- [ ] Configuration externalized appropriately
- [ ] Logging and monitoring in place
- [ ] Rollback plan defined (if needed)

---

## Notes & Considerations

### Open Questions

- List any unresolved questions or decisions needed
- Note areas where clarification is required
- Dependencies on external teams or resources
- Technical unknowns to investigate

### Future Enhancements

- Potential features for future iterations
- Known limitations to address later
- Technical debt to track
- Performance optimizations for later

### Related Specifications

- Link to related specs or requirements documents
- Dependencies on other components or features
- Relevant external documentation or resources
- Design documents or architectural decision records (ADRs)

### Risks and Mitigation

- Technical risks and how to address them
- Dependencies on external systems
- Performance bottlenecks
- Security concerns
