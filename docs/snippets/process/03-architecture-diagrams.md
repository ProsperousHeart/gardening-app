## Architecture Diagram Creation

This phase creates visual representations of system design to communicate technical architecture clearly via 3 required formats:

- Text
- ASCII
- Mermaid

### Purpose

Architecture diagrams provide a visual understanding of:
- System components and their relationships
- Data flows between components
- Integration points with external systems
- Technical architecture decisions
- Deployment structure

### When Diagrams Are Created

**CRITICAL**: Architecture diagrams are created **AFTER specifications** because they visualize the technical design decisions documented in the spec.

```
Requirements → Specifications → Architecture Diagrams → Threat Models
```

You need to know the system architecture, components, and data flows before you can diagram them.

### The Three-Format Requirement

**CRITICAL STANDARD**: All architecture diagrams MUST include THREE formats:

1. **Text Description** - Human-readable bullet points, tables, or numbered lists
2. **ASCII Diagram** - Text-based visual using box-drawing characters
3. **Mermaid Diagram** - Code block that renders as interactive diagram

This ensures:
- **Accessibility**: Text format for screen readers
- **Universal Viewing**: ASCII works everywhere (terminal, text editor, grep output)
- **Rich Visualization**: Mermaid provides interactive, styled diagrams

### The `/create-architecture` Command

**Format:**
```bash
/create-architecture <spec-or-name>
```

**Examples:**
```bash
# From specification file
/create-architecture docs/specifications/spec_genuser_plant-search.md

# From component name
/create-architecture user-authentication
```

### What This Command Does

1. **Reads Specification**
   - Analyzes technical architecture section
   - Identifies components and relationships
   - Extracts data flows and integration points

2. **Generates Three Diagram Formats**
   - **Text**: Component list with relationships
   - **ASCII**: Visual representation using ┌─┐│└┘ characters
   - **Mermaid**: Interactive diagram code

3. **Saves Diagram**
   - File: `docs/diagrams/architecture_{name}.md`
   - Includes all three formats
   - Adds metadata (date, spec reference)

4. **Updates Documentation**
   - Updates `docs/INDEX.md` with diagram link
   - Updates `docs/SPEC-CROSS-REFERENCE.md`
   - Links diagram to specification

### Diagram Types Supported

#### System Architecture Diagrams
Shows high-level system structure:
- User interfaces (web, mobile, CLI)
- Backend services
- Databases and storage
- External services and APIs

#### Component Diagrams
Shows internal component relationships:
- Modules and packages
- Dependencies between components
- Interface contracts
- Communication patterns

#### Sequence Diagrams
Shows interaction over time:
- Request/response flows
- Authentication sequences
- Multi-step processes
- Error handling flows

#### Entity Relationship Diagrams (ERD)
Shows data models:
- Database tables/collections
- Relationships (one-to-many, many-to-many)
- Key fields and constraints

#### Deployment Diagrams
Shows runtime environment:
- Servers and containers
- Network configuration
- Load balancers
- CDN and caching layers

### ASCII Box-Drawing Characters

Use these characters for ASCII diagrams:

```
┌─┐  Top border
│ │  Vertical sides
└─┘  Bottom border
├─┤  T-junctions
┼    Cross
→ ↓ ↑ ← Arrows
═    Double line (for emphasis)
```

**Example ASCII Diagram:**
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  API Layer  │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  Database   │
└─────────────┘
```

### Diagram Versioning

As architecture evolves, version diagrams:

**Approach 1: Version suffix**
- `architecture_user-auth-v1.md`
- `architecture_user-auth-v2.md`

**Approach 2: Date stamp**
- `architecture_user-auth-20251230.md`
- `architecture_user-auth-20260115.md`

**Recommendation**: Keep latest version without suffix, archive old versions in `docs/diagrams/archive/`

### Integration with Workflow

Architecture diagram creation is **automatically included** in the `/make-spec-from-req` workflow:

```bash
/make-spec-from-req docs/requirements/GenUser/req_genuser_plant-search.md
```

This generates:
1. Specification
2. **Architecture diagram** ← Automatic
3. Threat model
4. Documentation updates

You can also create diagrams independently:

```bash
/create-architecture docs/specifications/spec_genuser_plant-search.md
```

### Delegates To

- **Slash Command**: `.claude/commands/create-architecture.md`
- **Prompt**: `.github/prompts/create-architecture-diagram.prompt.md`
- **Instructions**: `.github/instructions/architecture-diagrams.instructions.md`

### Related Documentation

- **Architecture Instructions**: `.github/instructions/architecture-diagrams.instructions.md` (detailed format requirements)
- **Master Workflow**: `.github/instructions/master-workflow.md` (Stage 4)
- **Mermaid Documentation**: https://mermaid.js.org/

### Next Steps After Diagram Creation

1. **Review Diagram**: Verify accuracy of component relationships
2. **Stakeholder Feedback**: Ensure architecture is understandable
3. **Proceed to Threat Modeling**: Use diagram to identify security risks (**Phase 4**)
