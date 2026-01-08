Claude Code supports **autonomous agents** that can execute multi-step workflows with minimal human intervention. This provides the highest level of automation.

**Meta-Workflow Using Claude Code Agents:**

```markdown
## Automated Component Generation Workflow (Claude Code)

Execute this prompt to Claude Code to generate a complete component from requirements to implementation:

---

I need to generate a complete component following the SDD workflow. Please execute the following steps autonomously:

**Component**: {COMPONENT_NAME} (e.g., "01-general-user-plant-database")

### Phase 1: Research & Requirements Generation

1. **Use Explore Agent** (very thorough):
   - Analyze `docs/requirements/REQ-000b_Scope.md` for the {COMPONENT} section
   - Identify all performance criteria, data needs, and constraints
   - Review existing code in `2024-Django-Attempt/` if relevant
   - Compile comprehensive research summary

2. **Generate Requirement Document**:
   - Use `/create-requirement {COMPONENT_NAME}` slash command
   - OR manually create using `docs/templates/requirements-template.md`
   - Populate with research findings from Explore agent
   - Include CodeGuard security considerations
   - Map to REQ-000 series (with links)

3. **Review & Validate**:
   - Check all template sections complete
   - Verify links to REQ-000b work
   - Confirm success criteria are measurable
   - PAUSE for human review

**Human review checkpoint**: Review `docs/requirements/req-{XX}-{COMPONENT}.md` and approve to continue

---

### Phase 2: Specification Generation

4. **Execute Workflow Prompt**:
   \`\`\`
   Execute .github/prompts/workflow-requirements-to-spec.prompt.md for docs/requirements/req-{XX}-{COMPONENT}.md
   \`\`\`

   This automatically:
   - Generates detailed specification
   - Creates 3 diagram formats (Text, ASCII, Mermaid)
   - Creates STRIDE threat model
   - Runs quality review checklist
   - Updates SPEC-CROSS-REFERENCE.md

5. **Review & Validate**:
   - Verify three diagram formats present
   - Review threat model completeness
   - Check quality review passed
   - PAUSE for human review

**Human review checkpoint**: Review specification and diagrams, approve to continue

---

### Phase 3: TDD Implementation

6. **Execute Implementation Workflow**:
   /`/`/`
   Execute .github/prompts/workflow-spec-to-code.prompt.md for docs/specifications/spec-{XX}-{COMPONENT}.md
   /`/`/`

   This automatically:
   - Implements with TDD (Red → Green → Refactor)
   - Writes all tests first
   - Implements source code
   - Runs security review (CodeGuard)
   - Updates SPEC-CROSS-REFERENCE.md

7. **Verification**:
   Run in parallel:
   /`/`/`bash
   make lint
   make format
   make test
   \`\`\`

   Then run:
   \`\`\`
   /verify src/{COMPONENT}
   /security-review src/{COMPONENT}
   \`\`\`

8. **Track Progress**:
   - Use TodoWrite to track each phase
   - Mark phases complete as you go
   - Report any blockers immediately

**Human review checkpoint**: Review implementation, tests passing, security review passed

---

### Phase 4: Documentation & Completion

9. **Update Cross-Reference**:
   \`\`\`
   /update-docs spec-cross-ref req-{XX}-{COMPONENT}.md
   /`/`/`

10. **Document Lessons Learned**:
    - Update `docs/Process.md` with:
      - What worked well
      - Workflow bottlenecks encountered
      - Optimizations discovered
      - CodeGuard learnings

11. **Create Summary**:
    - Provide completion summary
    - List all files created
    - Report test coverage
    - Highlight any deviations from plan

---

**IMPORTANT**:
- Use TodoWrite at start of each phase to track progress
- Pause for human review at each checkpoint
- Use agents (Explore, Plan) for research and planning
- Use workflow prompts for specification and implementation
- Document blockers immediately

End of workflow.
```

**Key Claude Code Advantages:**

✅ **Autonomous Agents**: Explore agent does deep research automatically
✅ **Slash Commands**: Direct integration with workflow prompts
✅ **TodoWrite**: Automatic progress tracking throughout workflow
✅ **File Operations**: Reads/writes files directly, no copy/paste
✅ **Multi-Tool Coordination**: Agents + prompts + bash commands in single workflow
✅ **Parallel Execution**: Can run multiple tasks simultaneously
✅ **Context Awareness**: Maintains full conversation context across all steps

**Example Usage:**

```
Generate the plant database component using the automated workflow above
```

Claude Code will then autonomously:

1. Research using Explore agent
2. Generate requirements
3. Generate specifications with diagrams
4. Implement with TDD
5. Run verification
6. Update documentation
7. Track progress with todos
8. Pause only for human review checkpoints