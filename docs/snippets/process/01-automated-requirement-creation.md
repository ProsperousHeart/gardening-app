## Automated Requirement Creation Workflow

This section documents the creation and refinement of automation commands for streamlined requirement management.

### Background

To improve the efficiency of creating requirements and specifications, two complementary slash commands were developed:

1. **`/create-requirement`** - Creates a new requirement document from template
2. **`/make-spec-from-req`** - Generates technical specification from an existing requirement

### Understanding the Difference

These commands serve different purposes in the specification-driven development workflow:

| Aspect | `/create-requirement` | `/make-spec-from-req` |
|--------|----------------------|----------------------|
| **Purpose** | Creates NEW requirement document | Generates specification FROM existing requirement |
| **Input** | Subsystem + Component name | Path to completed requirement file |
| **Output** | Empty template with placeholders | Technical spec + architecture + threat model |
| **Stage** | Step 1: Requirement Creation | Step 2: Specification Generation |
| **Human Work** | AFTER (fill in requirement details) | BEFORE (requirement must be complete) |
| **File Created** | `docs/requirements/{subsystem}/req_{subsystem}_{component}.md` | `docs/specifications/spec_{component}.md` |

### Complete Workflow Example

Here's how these commands work together:

```bash
# STEP 1: Create requirement template
/create-requirement genuser plant-search

# Output: Creates docs/requirements/genuser/req_genuser_plant-search.md
# This is an EMPTY template with placeholders like:
#   [Description of what this feature does]
#   [Acceptance criteria go here]
#   [Security considerations]

# STEP 2: Human fills in requirement details
# Open docs/requirements/genuser/req_genuser_plant-search.md
# Replace all placeholders with actual requirements
# Define acceptance criteria, constraints, dependencies, etc.

# STEP 3: Generate specification from completed requirement
/make-spec-from-req docs/requirements/genuser/req_genuser_plant-search.md

# Output: Creates multiple artifacts:
#   - docs/specifications/spec_genuser_plant-search.md
#   - docs/diagrams/architecture_genuser_plant-search.md
#   - docs/diagrams/threat-model_genuser_plant-search.md
#   - Updates SPEC-CROSS-REFERENCE.md and INDEX.md
```

### Command Details: `/create-requirement`

**Format:**

```bash
/create-requirement <subsystem> <component-name>
```

**Examples:**

- `/create-requirement sysadmin user-authentication`
- `/create-requirement genuser plant-search`
- `/create-requirement communitylead plot-management`

**What It Does:**

1. **Validates Prerequisites**

    - Checks that `docs/templates/requirements-template.md` exists
    - Ensures `docs/requirements/{subsystem}/` directory exists (creates if missing)
    - Checks for existing requirement files to prevent overwrites

2. **Creates Requirement Document**

    - Reads template at `docs/templates/requirements-template.md`
    - Generates new file at `docs/requirements/{subsystem}/req_{subsystem}_{component-name}.md`
    - Fills in placeholders with helpful guidance comments
    - Preserves template structure (Overview, Functional Requirements, etc.)

3. **Updates Documentation**

    - Adds entry to `docs/SPEC-CROSS-REFERENCE.md` (status: 📝 Requirement Defined)
    - Adds link to `docs/INDEX.md` under Requirements section
    - Validates requirement index files updated appropriately

**Directory Structure:**

Requirements are organized by subsystem for better organization:

```
docs/requirements/
├── GenUser/          # General user features (plant search, weather, etc.)
├── sysadmin/         # System administration features
├── CommunityLead/    # Community leader features (plot assignment, etc.)
└── CommunityMember/  # Community member features (chore tracking, etc.)
```

**Delegates To:**

- Slash command: `.claude/commands/create-requirement.md`
- Core logic: `.github/prompts/create-requirement.prompt.md`

### Command Details: `/make-spec-from-req`

**Format:**

```bash
/make-spec-from-req <requirement-file-path> [threat-model-scope]
```

**Examples:**

- `/make-spec-from-req docs/requirements/genuser/req_genuser_plant-search.md`
- `/make-spec-from-req docs/requirements/sysadmin/req_sysadmin_user-auth.md high-level-aggregate`

**What It Does:**

This is a **workflow orchestration command** that executes multiple steps:

1. **Generate Specification**

    - Reads completed requirement document
    - Generates detailed technical specification
    - Includes architecture decisions, data flows, integration points
    - Documents security considerations with CodeGuard references

2. **Create Architecture Diagram**

    - Generates three diagram formats (Text, ASCII, Mermaid)
    - Shows system components and relationships
    - Saved to `docs/diagrams/architecture_{name}.md`

3. **Create Threat Model**

    - Applies STRIDE framework (Spoofing, Tampering, Repudiation, etc.)
    - Identifies security risks based on specification
    - Documents mitigations and CodeGuard compliance
    - Saved to `docs/diagrams/threat-model_{name}.md`

4. **Run Quality Review**

    - Validates all required sections present
    - Checks for broken links
    - Ensures documentation standards followed

5. **Update Documentation**

    - Updates `docs/SPEC-CROSS-REFERENCE.md` (status: 🔍 Specified)
    - Updates `docs/INDEX.md` with new specification links
    - Logs execution to `docs/output-logs/{timestamp}-spec-workflow.md`

**Threat Model Scope Options:**

- `per-requirement` (default) - Feature-specific threat model
- `high-level-aggregate` - System-wide security view
- `grouped-by-feature` - Module-level threat model

**Delegates To:**

- Slash command: `.claude/commands/make-spec-from-req.md`
- Core logic: `.github/prompts/workflow-requirements-to-spec.prompt.md`

### Key Insights

**Why Two Separate Commands?**

1. **Separation of Concerns**: Creating templates vs. generating specifications are distinct operations
2. **Human-in-the-Loop**: Requirement creation produces a template that humans fill in with domain knowledge
3. **AI Strengths**: Specification generation leverages AI to translate requirements into technical architecture
4. **Workflow Clarity**: Makes the two-step process explicit (Create → Fill → Generate)

**Common Mistake to Avoid:**

❌ **WRONG**: Running `/make-spec-from-req` immediately after `/create-requirement`

- The requirement file is still empty with placeholders!
- Specification will be generated from incomplete information

✅ **CORRECT**: Fill in requirement details first, THEN generate specification

- Human provides domain knowledge and acceptance criteria
- AI generates technical specification from complete requirements

### Refinements Made

**Version 1 (Initial):**

- Single parameter: component name only
- Files saved directly to `docs/requirements/`
- Manual organization required

**Version 2 (Current):**

- Two parameters: subsystem + component name
- Automatic subsystem directory organization
- Better scalability as project grows
- Consistent naming: `req_{subsystem}_{component-name}.md`

### Related Documentation

- **Requirement Template**: `docs/templates/requirements-template.md`
- **Specification Template**: `docs/templates/spec-template.md`
- **Master Workflow**: `.github/instructions/master-workflow.md`
- **All Slash Commands**: `.claude/commands/README.md`
- **Workflow Prompts**: `.github/prompts/README.md`
