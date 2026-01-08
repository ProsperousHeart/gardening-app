GitHub Copilot requires more manual orchestration since it lacks autonomous agents and slash commands. The workflow is more stepwise and IDE-integrated.

**Meta-Workflow Using GitHub Copilot:**

```markdown
## Manual Component Generation Workflow (GitHub Copilot)

Use this checklist to guide GitHub Copilot through the SDD workflow step-by-step.

**Component**: {COMPONENT_NAME} (e.g., "01-general-user-plant-database")

---

### Phase 1: Research & Requirements Generation

1. **Manual Research**:
   - Open `docs/requirements/REQ-000b_Scope.md`
   - Locate the {COMPONENT} section manually
   - Read performance criteria, data needs, constraints
   - Review `2024-Django-Attempt/` code if relevant
   - Take notes in a scratch file

2. **Generate Requirement Document**:
   - Copy `.github/prompts/create-requirement.prompt.md` content
   - Open Copilot Chat
   - Paste prompt with @workspace context:
     ```
     @workspace Using the prompt from .github/prompts/create-requirement.prompt.md,
     create a requirement document for "{COMPONENT_NAME}"

     Include context from:
     - docs/requirements/REQ-000b_Scope.md #{SECTION}
     - docs/templates/requirements-template.md
     - 2024-Django-Attempt/Plants/models.py (if relevant)
     ```

3. **Create File Manually**:
   - Copy Copilot's output
   - Create `docs/requirements/req-{XX}-{COMPONENT}.md`
   - Paste content
   - Manually add missing sections
   - Add CodeGuard security considerations
   - Add links to REQ-000b sections

4. **Review Checklist** (manual):
   - [ ] All template sections complete?
   - [ ] Links to REQ-000b working?
   - [ ] Success criteria measurable?
   - [ ] CodeGuard considerations included?

---

### Phase 2: Specification Generation

5. **Generate Specification**:
   - Copy `.github/prompts/generate-spec-from-requirement.prompt.md`
   - Open Copilot Chat
   - Paste prompt with context:
     ```
     @workspace Using the prompt from .github/prompts/generate-spec-from-requirement.prompt.md,
     create a specification from docs/requirements/req-{XX}-{COMPONENT}.md

     Include context from:
     - docs/templates/spec-template.md
     - docs/requirements/req-{XX}-{COMPONENT}.md
     ```

6. **Create Specification File**:
   - Copy output
   - Create `docs/specifications/spec-{XX}-{COMPONENT}.md`
   - Paste content

7. **Generate Architecture Diagram**:
   - Copy `.github/prompts/create-architecture-diagram.prompt.md`
   - Open Copilot Chat
   - Paste prompt:
     ```
     @workspace Create architecture diagram for spec-{XX}-{COMPONENT}.md
     following .github/prompts/create-architecture-diagram.prompt.md

     IMPORTANT: Include all three formats:
     1. Text description
     2. ASCII diagram
     3. Mermaid diagram
     ```
   - Copy output
   - Create `docs/diagrams/arch-{XX}-{COMPONENT}.md`
   - Paste content

8. **Generate Threat Model**:
   - Copy `.github/prompts/create-threat-model.prompt.md`
   - Open Copilot Chat
   - Paste prompt:
     ```
     @workspace Create STRIDE threat model for spec-{XX}-{COMPONENT}.md
     following .github/prompts/create-threat-model.prompt.md
     ```
   - Copy output
   - Create `docs/diagrams/threat-{XX}-{COMPONENT}.md`
   - Paste content

9. **Review Checklist** (manual):
   - [ ] Specification complete?
   - [ ] Three diagram formats present?
   - [ ] Threat model covers all STRIDE categories?
   - [ ] Quality review checklist passed?

---

### Phase 3: TDD Implementation

10. **Generate Test Files**:
    - Copy `.github/prompts/testcase.prompt.md`
    - Open Copilot Chat:
      ```
      @workspace Generate tests for spec-{XX}-{COMPONENT}.md
      following TDD workflow from .github/instructions/tdd-workflow.instructions.md

      Create test files in tests/ following the specification
      ```
    - Copy test code
    - Create test files manually
    - Run tests (should fail - RED phase)

11. **Implement Source Code**:
    - Open Copilot Chat:
      ```
      @workspace Implement source code to pass the tests I just created
      for spec-{XX}-{COMPONENT}.md

      Follow Django best practices and CodeGuard security rules
      ```
    - Copy source code
    - Create source files manually
    - Run tests (should pass - GREEN phase)

12. **Refactor**:
    - Open Copilot Chat:
      ```
      @workspace Review the implementation and suggest refactoring improvements
      while keeping tests passing
      ```
    - Apply suggestions manually

13. **Run Verification** (manual terminal):
    ```bash
    make lint
    make format
    make test
    ```

14. **Security Review**:
    - Copy `.github/prompts/security-review.prompt.md`
    - Open Copilot Chat:
      ```
      @workspace Review src/{COMPONENT} for security issues
      following .github/prompts/security-review.prompt.md

      Check against CodeGuard rules
      ```
    - Review output
    - Fix issues manually

---

### Phase 4: Documentation & Completion

15. **Update Cross-Reference** (manual):
    - Open `docs/SPEC-CROSS-REFERENCE.md`
    - Add new row with links to:
      - Requirement file
      - Specification file
      - Source files
      - Test files
      - Diagram files
    - Update status to "Implemented"

16. **Update Process Documentation** (manual):
    - Open `docs/Process.md`
    - Document lessons learned
    - Update workflow steps if needed

17. **Final Checklist** (manual):
    - [ ] All files created?
    - [ ] Tests passing?
    - [ ] Linting passing?
    - [ ] Security review passed?
    - [ ] Cross-reference updated?
    - [ ] Process.md updated?

---

**End of Copilot Workflow**
```

**Key GitHub Copilot Characteristics:**

⚠️ **Manual Orchestration**: Each step requires explicit prompting

⚠️ **Copy/Paste Workflow**: Must manually copy outputs to files

⚠️ **No Agents**: Cannot autonomously research or plan

⚠️ **IDE-Integrated**: Works within VS Code, good for editing

⚠️ **Context via @workspace**: Uses workspace files for context

⚠️ **Step-by-Step**: Cannot execute multi-step workflows autonomously

⚠️ **No Progress Tracking**: No built-in todo/progress tracking

**Example Usage:**

Each step requires a separate chat message like:
```
@workspace Using .github/prompts/create-requirement.prompt.md,
create requirement for "01-general-user-plant-database"
```

Then manually create the file and paste the output.