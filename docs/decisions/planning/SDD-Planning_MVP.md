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

--8<-- "decisions\planning\SDD-Planning_MVP\MVP_overview.md:overview"

---

--8<-- "decisions\planning\SDD-Planning_MVP\MVP_req-gen-strategy.md"

---

--8<-- "decisions\planning\SDD-Planning_MVP\MVP_PRI_Based_Order.md"

---

--8<-- "decisions\planning\SDD-Planning_MVP\MVP_Reqs_By_GenAI.md"

---

--8<-- "decisions\planning\SDD-Planning_MVP\MVP_GenAI_Agents-n-Prompts.md"

---

--8<-- "snippets\technical\Code_Guard_Integration.md"

---

## Workflow Execution Plan

### Step-by-Step Execution

#### Prerequisites

1. **Environment Setup**:

   **Claude Code:**
   ```bash
   /setup-env
   ```

   **GitHub Copilot:**
   ```
   Execute .github/instructions/uv-environment-setup.instructions.md
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

    **Claude Code:**
    ```bash
    /create-requirement general-user-plant-database
    ```

    **GitHub Copilot:**
    ```
    Execute .github/prompts/create-requirement.prompt.md for "general-user-plant-database"
    ```

    **Output:** `docs/requirements/req-general-user-plant-database.md`

2. **Manual Review**:
    - Verify all sections complete
    - Cross-reference with REQ-000b: `System.GenUser.ViewsAndInsights.PlantDatabase`
    - Add CodeGuard security considerations
    - Review data model against `2024-Django-Attempt/Plants/models.py`

3. **Generate Specification**:

    **Claude Code:**
    ```bash
    /make-spec-from-req docs/requirements/req-general-user-plant-database.md
    ```

    **GitHub Copilot:**
    ```
    Execute .github/prompts/workflow-requirements-to-spec.prompt.md for docs/requirements/req-general-user-plant-database.md
    ```

    **Outputs:**

    - `docs/specifications/spec-general-user-plant-database.md`
    - `docs/diagrams/arch-general-user-plant-database.md`
    - `docs/diagrams/threat-general-user-plant-database.md`

4. **Manual Review**:

    - Verify three diagram formats (Text, ASCII, Mermaid)
    - Review threat model (STRIDE)
    - Validate against quality checklist

5. **Implement with TDD**:

    **Claude Code:**
    ```bash
    /implement-spec docs/specifications/spec-general-user-plant-database.md
    ```

    **GitHub Copilot:**
    ```
    Execute .github/prompts/workflow-spec-to-code.prompt.md for docs/specifications/spec-general-user-plant-database.md
    ```

    **Outputs:**

    - Source files: `src/plants/models.py`, etc.
    - Test files: `tests/test_plants.py`, etc.

6. **Verify Implementation**:

    **Standard commands (both Claude Code and GitHub Copilot):**

    ```bash
    make lint
    make format
    make test
    ```

    **Claude Code:**

    ```bash
    /verify src/plants
    /security-review src/plants
    ```

    **GitHub Copilot:**

    ```
    Execute .github/prompts/verify-implementation.prompt.md for src/plants
    Execute .github/prompts/security-review.prompt.md for src/plants
    ```

7. **Update Cross-Reference**:

    **Claude Code:**

    ```bash
    /update-docs spec-cross-ref req-general-user-plant-database.md
    ```

    **GitHub Copilot:**

    ```
    Execute .github/prompts/update-documentation.prompt.md for spec-cross-ref req-general-user-plant-database.md
    ```

**Requirement 2: Plant Search & Filter**

Repeat steps 1-7 for:

- `req-general-user-plant-search.md`
- `req-general-user-plant-filter.md`

---

#### Phase 2: Supporting Calculations & Data

Repeat steps 1-7 for:

- `req-general-user-calculations.md`
- `req-general-user-usda-zones.md`

---

#### Phase 3: User Experience Enhancements

Repeat steps 1-7 for:

- `req-general-user-weather.md`
- `req-general-user-notifications.md`
- `req-general-user-general-resources.md`

---

#### Phase 4: User Data & Feedback

Repeat steps 1-7 for:

- `req-general-user-feedback.md`
- `req-general-user-account-favorites.md`
- `req-general-user-add-plant.md`

---

#### Phase 5: Advanced General Features

Repeat steps 1-7 for:

- `req-general-user-moon-gardening.md`
- `req-general-user-pest-database.md`

---

#### Phase 6: Community Features

Repeat steps 1-7 for:

- `req-community-member-announcements.md`
- `req-community-member-plot-management.md`
- `req-community-member-team-chores.md`
- `req-community-member-apprentice-program.md`

---

#### Phase 7: Admin Features - DEFERRED

Only proceed after Phases 1-6 complete and deployed:

- `req-admin-account-management.md`
- `req-admin-educator-role.md`
- `req-admin-elevated-access.md`

---

### Automation Opportunities

The **meta-workflow** process differs significantly between Claude Code and GitHub Copilot due to their different capabilities. This section compares multiple approaches.

#### bash

Consider creating a bash **meta-workflow script** to automate the repetitive steps:

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

#### AI Integration | Claude Code: Agent-Based Automation (Recommended)

!!! note
    The information below comes from [this snippet](../../snippets/technical/Claude-Code-Agent-Automation.md)

---8<-- "snippets\technical\Claude-Code-Agent-Automation.md"

---

#### GitHub Copilot: Manual Prompt-Based Workflow

!!! note
    The information below comes from [this snippet](../../snippets/technical/Copilot_Req_Automation.md)

---8<-- "snippets\technical\Copilot_Req_Automation.md"

---

#### Comparison Summary

| Feature | Bash Script | Claude Code (Agents) | GitHub Copilot (Chat) |
|---------|-------------|---------------------|----------------------|
| **Workflow Automation** | High - fixed workflow orchestration | High - intelligent, adaptive workflow | Low - manual step-by-step prompting |
| **Adaptability** | None - follows hardcoded logic paths | High - adapts to context, errors, findings | Medium - adapts per manual prompt |
| **Research Capability** | None - requires pre-populated data | Explore agent does deep, autonomous research | Manual research + @workspace context |
| **File Operations** | Shell commands (grep, sed, awk, etc.) | Direct read/write/edit with AI understanding | Manual copy/paste to files |
| **Progress Tracking** | Echo statements + manual tracking | TodoWrite automatic tracking | Manual checklist tracking |
| **Slash Commands** | Calls slash commands via bash | Native `/command` support | Must copy prompts manually |
| **Multi-Step Workflows** | Yes - orchestrates commands/scripts | Yes - executes and coordinates steps | Yes - can generate multi-step plan with prompt refs |
| **Multi-Step Execution** | Fully automated execution | Fully automated execution | Manual execution of each step |
| **Context Awareness** | Syntax only - no semantic understanding | Full semantic understanding + file system | @workspace files with AI understanding |
| **Parallel Execution** | Yes - `&`, `wait`, `xargs -P`, etc. | Yes - multiple tools simultaneously | No - sequential only |
| **Error Handling** | If/else logic - must code all cases | AI reasoning about errors and solutions | AI suggests fixes, human implements |
| **Review Checkpoints** | Manual `read` prompts | Built-in pause/resume | Manual checkpoints |
| **AI-Powered** | No - shell scripting only | Yes - full Claude Code capabilities | Yes - GitHub Copilot AI |
| **Best For** | Repeatable, fixed workflows | Dynamic, context-aware generation | Step-by-step guided development |
| **Human Effort** | Low - run script, review at checkpoints | Low - mostly review and approve | High - orchestrate every step |
| **Setup Complexity** | Medium - write and maintain script | None - built-in capability | None - built-in capability |
| **Workflow Changes** | Requires script editing | AI adapts automatically | Requires different prompts |

**Recommendation**:

- **Use Bash Script** for repeatable automation of existing slash commands (good for batch processing)
- **Use Claude Code** for intelligent, context-aware component generation with autonomous agents
- **Use GitHub Copilot** for individual code editing and refinement within IDE
- **Hybrid Approach**: Bash for workflow orchestration + Claude Code for AI assistance + Copilot for in-IDE editing

---

#### Practical Example: Generating Plant Database Component

**With Claude Code (Single Prompt):**

```
Generate the plant database component (req-general-user-plant-database)
following the automated workflow. Use Explore agent for research, execute
workflow prompts for spec and implementation, track progress with todos,
and pause for my review after each phase.
```

→ Claude Code autonomously completes all 4 phases with 3 review checkpoints

**With GitHub Copilot (15+ Manual Steps):**

```
Step 1:
@workspace Using .github/prompts/create-requirement.prompt.md...
[copy output to file]

Step 2:
@workspace Using .github/prompts/generate-spec-from-requirement.prompt.md...
[copy output to file]

Step 3:
@workspace Create architecture diagram...
[copy output to file]

... (12 more manual steps)
```

→ Requires manual prompting and file creation for each step

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

2. **Start with Phase 1, Requirement 1**:

    - Generate `req-general-user-plant-database.md`
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
6. **First Component**: Ready to start with `req-general-user-plant-database.md`?

---

**End of Planning Document**

This plan will evolve as we learn and optimize the SDD workflow. All changes should be documented in `docs/Process.md` for future reference and training.
