---
title: Agents and Prompts to Use for GenAI Created MVP
description: GenAI suggested agents & prompts to generate. Still needs to be reviewed as of 20251227 for alignment with original MVP plans. It also seems to be for more than just an MVP.
---

## [Agents and Prompts to Use](./MVP_GenAI_Agents-n-Prompts.md)

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
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-general-user-plant-database.md
```

**Outputs:**

- `docs/specifications/spec-general-user-plant-database.md`
- `docs/diagrams/arch-general-user-plant-database.md`
- `docs/diagrams/threat-general-user-plant-database.md`
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
Execute the workflow-spec-to-code prompt for docs/specifications/spec-general-user-plant-database.md
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
Use the Task tool with subagent_type='Explore' to analyze the existing Plant model in 2024-Django-Attempt/Plants/models.py and identify all fields that should be included in req-general-user-plant-database.md
```

**Thoroughness levels**: `quick`, `medium`, `very thorough`

---

#### Plan Agent (for architecture planning)

**When to use**: Designing implementation strategy before writing specs

**Example**:

```
Use the Task tool with subagent_type='Plan' to design the plant search API architecture for req-general-user-plant-search.md
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