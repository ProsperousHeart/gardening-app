## Specification Generation Workflow

This phase converts completed requirements into detailed technical specifications with architecture decisions, security considerations, and implementation guidance.

### Background

After requirements are created and filled in, the next step is to generate a technical specification that translates business requirements into actionable technical details. This phase was developed to automate the creation of specifications, architecture diagrams, and threat models in a single orchestrated workflow.

### The `/make-spec-from-req` Workflow

This is a **workflow orchestration command** that executes multiple steps automatically:

**Format:**

```bash
/make-spec-from-req <requirement-file-path> [threat-model-scope]
```

**Examples:**

```bash
/make-spec-from-req docs/requirements/GenUser/req_genuser_plant-search.md
/make-spec-from-req docs/requirements/SysAdmin/req_sysadmin_user-auth.md high-level-aggregate
```

### What This Workflow Does

The specification generation workflow orchestrates **4 major steps**:

#### Step 1: Pre-flight Validation

- Verifies requirement file exists and is complete
- Checks for required templates (spec-template.md)
- Validates requirement has all necessary sections filled in
- Ensures no placeholder text remains

#### Step 2: Generate Specification

- Reads completed requirement document
- Uses `docs/templates/spec-template.md` as structure
- Generates detailed technical specification including:
  - **Technical Architecture**: System design decisions
  - **Data Models**: Database schemas and relationships
  - **API Design**: Endpoints, request/response formats
  - **Integration Points**: How this integrates with other components
  - **Security Considerations**: CodeGuard rule references
  - **TDD Planning**: Test strategy and test cases
  - **Implementation Guidance**: Step-by-step approach

**Output**: `docs/specifications/spec_{name}.md`

#### Step 3: Create Architecture Diagram

- Automatically generates architecture diagram from specification
- **CRITICAL**: Must include THREE formats (Text, ASCII, Mermaid)
- Shows components, relationships, data flows
- Documents integration points

**Output**: `docs/diagrams/architecture_{name}.md`

See **Phase 3: Architecture Diagrams** for details.

#### Step 4: Create Threat Model

- Applies STRIDE framework (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege)
- Identifies security risks based on specification and architecture
- Maps threats to CodeGuard security rules
- Documents mitigations and security requirements

**Output**: `docs/diagrams/threat-model_{name}.md`

**IMPORTANT**: Threat modeling happens AFTER specifications because you need to know the system architecture, data flows, and technical approach before identifying security threats.

See **Phase 4: Threat Modeling** for details.

#### Step 5: Quality Review

- Validates all required sections present in spec
- Checks for broken links
- Ensures documentation standards followed
- Verifies CodeGuard references are valid

#### Step 6: Update Documentation

- Updates `docs/SPEC-CROSS-REFERENCE.md` (status: 🔍 Specified)
- Updates `docs/INDEX.md` with new specification links
- Logs execution to `docs/output-logs/{timestamp}-spec-workflow.md`

### Threat Model Scope Options

The workflow accepts an optional scope parameter to control threat model granularity:

| Scope | When to Use | What It Covers |
|-------|-------------|----------------|
| `per-requirement` (default) | Individual features | Feature-specific threats and mitigations |
| `high-level-aggregate` | System overview | System-wide security view, cross-cutting concerns |
| `grouped-by-feature` | Related features | Module-level threats for related components |

**Example with scope:**

```bash
/make-spec-from-req docs/requirements/SysAdmin/req_sysadmin_user-auth.md high-level-aggregate
```

### Historical Context: Creating the Workflow

This section documents how the specification generation workflow was originally developed.

#### Initial Approach (Manual)

1. Ensured the [spec-template.md](./templates/spec-template.md) was created
2. Ran `/init` for Claude to understand existing structure
3. Created the [general-app-spec-ORIGINAL.md](../specs/general-app-spec-ORIGINAL.md)
4. Created [`general-app-requirements`](./requirements/for-sdd/general-app-requirements.md) with stakeholder input

#### Evolution to Automation

Early workflow development involved manual steps:

```markdown
Generate specs for a gardener app using @templates/spec-template.md
Build the specs in such a way that the different pieces or milestones
can be built independently instead of all at once.

[Requirements for 3 main sections: GeneralUser, GardenGroups, AdminAccess]

# Constraints

- Python Django
- Next.js 15 App Router with React 19
- Tailwind for CSS styling
```

This manual approach was refined into the automated `make-spec-from-req` command.

#### Creating the Command

**Step 1**: Created initial command `make-spec-from-req.md`:

```markdown
---
argument-hint: [component-name] [req-file]
description: Create a spec file from requirements file
---

Generate a spec for $1 using @templates/spec-template.md and $2

Add a section to your spec titled "Integration Architecture" that includes:

- component interaction diagram (in text/markdown)
- data flow description
- key integration points
- dependencies on previously created specs
```

**Step 2**: Ran optimization request:

```
How might I improve @commands\make-spec-from-req.md to build a spec from
@templates\spec-template.md and a requirement file? how should requirement
file be set up? Please provide an example template in @templates
```

This led to:
- Creation of `requirements-template.md`
- Refinement of the command to include architecture diagrams
- Addition of threat modeling
- Integration of quality review steps

**Step 3**: Evolved to orchestration workflow:

The command was enhanced to orchestrate multiple phases:
- Spec generation
- Architecture diagram creation
- Threat model generation
- Quality review
- Documentation updates

This became the `workflow-requirements-to-spec.prompt.md` orchestration prompt.

### Key Insights

**Why Orchestration?**

1. **Consistency**: Same steps executed every time
2. **Efficiency**: Multiple artifacts generated in one command
3. **Quality**: Built-in review checks
4. **Traceability**: Automatic documentation updates

**Why Threat Models After Specs?**

You cannot identify security threats without knowing:
- System architecture and components
- Data flows and integrations
- Trust boundaries
- Attack surface

Specifications provide this context, making threat modeling accurate and comprehensive.

**Specification as Hub**

The specification document serves as the central hub linking:
- **Backward**: To requirements (what we're building and why)
- **Forward**: To code and tests (implementation)
- **Sideways**: To diagrams and threat models (understanding and security)

### Delegates To

- **Slash Command**: `.claude/commands/make-spec-from-req.md`
- **Orchestration Prompt**: `.github/prompts/workflow-requirements-to-spec.prompt.md`
- **Individual Spec Prompt**: `.github/prompts/generate-spec-from-requirement.prompt.md`
- **Architecture Prompt**: `.github/prompts/create-architecture-diagram.prompt.md`
- **Threat Model Prompt**: `.github/prompts/create-threat-model.prompt.md`

### Related Documentation

- **Specification Template**: `docs/templates/spec-template.md`
- **Architecture Instructions**: `.github/instructions/architecture-diagrams.instructions.md`
- **Threat Modeling Instructions**: `.github/instructions/threat-modeling.instructions.md`
- **Quality Checklist**: `.github/instructions/quality-checklists.md` (Specification Stage)
- **Master Workflow**: `.github/instructions/master-workflow.md` (Stage 3)

### Next Steps After Specification Generation

1. **Human Review**: Review spec, architecture diagram, and threat model
2. **Stakeholder Approval**: Ensure technical approach meets requirements
3. **Ready for Implementation**: Proceed to **Phase 5: TDD Implementation**
