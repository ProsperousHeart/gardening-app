# Meta-Documentation Checklist

**Purpose**: Ensure documentation stays synchronized when creating or modifying prompts, commands, and instructions.

**IMPORTANT**: AI assistants should follow this checklist whenever creating or modifying documentation in `.github/` or `.claude/`.

## ✅ Creating a New Prompt

When creating a new file in `.github/prompts/`:

- [ ] Create the prompt file: `.github/prompts/{name}.prompt.md`
- [ ] Follow the standard prompt structure (see `.github/prompts/README.md`)
- [ ] Add entry to `.github/prompts/README.md` in the appropriate section
- [ ] If the prompt should be user-accessible, create Claude command: `.claude/commands/{name}.md`
- [ ] Add entry to `.claude/commands/README.md` table
- [ ] Update `CLAUDE.md` slash commands table if applicable
- [ ] Update CHANGELOG.md with the new files
- [ ] Add example usage to `.github/instructions/claude-usage.instructions.md`
- [ ] Add example usage to `.github/instructions/copilot-usage.instructions.md`

## ✅ Creating a New Claude Command

When creating a new file in `.claude/commands/`:

- [ ] Ensure corresponding prompt exists in `.github/prompts/`
- [ ] Follow delegation pattern: `Execute the prompt at .github/prompts/{name}.prompt.md`
- [ ] Include parameter syntax: `{{$1}}` for required, `{{$2|default}}` for optional
- [ ] Add usage examples showing both parameter styles
- [ ] Document expected output
- [ ] Add entry to `.claude/commands/README.md` table
- [ ] Update `CLAUDE.md` slash commands table
- [ ] Update CHANGELOG.md
- [ ] Test the command works before committing

## ✅ Creating a New Instruction File

When creating a new file in `.github/instructions/`:

- [ ] Create the instruction file: `.github/instructions/{name}.instructions.md`
- [ ] Add clear step-by-step guidance
- [ ] Include examples where helpful
- [ ] Add entry to `.github/instructions/README.md` in appropriate section
- [ ] Reference from relevant prompts in `.github/prompts/`
- [ ] Update `CLAUDE.md` if it's a core workflow instruction
- [ ] Update CHANGELOG.md
- [ ] Add to quality checklists if applicable

## ✅ Modifying an Existing Workflow

When changing workflow logic:

- [ ] Update the generic prompt in `.github/prompts/`
- [ ] Update corresponding Claude command in `.claude/commands/` if it exists
- [ ] Update workflow documentation in `.github/instructions/master-workflow.md`
- [ ] Update quality checklists in `.github/instructions/quality-checklists.md` if applicable
- [ ] Update CHANGELOG.md with the changes
- [ ] Add migration notes if the change affects existing usage
- [ ] Test the workflow end-to-end

## ✅ Deprecating/Archiving Documentation

When removing or archiving:

- [ ] Move file to `.archive/` subdirectory (don't delete)
- [ ] Remove from README.md tables/lists
- [ ] Add deprecation note to CHANGELOG.md
- [ ] Update any references in other files
- [ ] Add redirect comment in archived file pointing to replacement (if any)
- [ ] Update `CLAUDE.md` if it was referenced there

## 📋 Documentation Standards

All documentation files should:

- [ ] Include "Last Updated" date at the top
- [ ] Use consistent markdown formatting (see `docs/rules/markdown-standards.md`)
- [ ] Include clear examples
- [ ] Reference related documentation
- [ ] Use proper heading hierarchy
- [ ] Include a purpose/overview section

## 🔍 Validation Checklist

Before committing documentation changes:

- [ ] All internal links work (no broken references)
- [ ] README files are updated
- [ ] CHANGELOG.md has an entry
- [ ] Examples are correct and tested
- [ ] Cross-references are bidirectional (if A references B, should B reference A?)
- [ ] Markdown linting passes (`ruff check` if configured)
- [ ] No duplicate information across files (prefer references)

## 🔄 Periodic Review

Every quarter, review:

- [ ] Are all prompts still used? Archive unused ones
- [ ] Are all commands still needed? Archive obsolete ones
- [ ] Do README files accurately reflect current state?
- [ ] Are there new patterns that should be documented?
- [ ] Are there duplicated instructions that should be consolidated?

---

**Last Updated**: 2025-11-10