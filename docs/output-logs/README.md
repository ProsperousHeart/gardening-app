# Workflow Output Logs

This folder contains execution logs from workflow operations performed in the `docs/` context.

## 📋 Purpose

Output logs provide:
- Record of operations performed
- Execution details for documentation workflows
- Audit trail for doc generation
- Troubleshooting information

## 📁 Log Types

This folder is for **documentation workflow logs**:
- Requirement creation
- Specification generation
- Cross-reference updates
- Index updates

For **code generation and AI prompt execution logs**, see:
- `.github/prompts/output-logs/` - Main AI prompt execution logs

## 📝 Log Format

Follow the format defined in `docs/rules/output-format.md`.

## 🗑️ Cleanup

Logs can be deleted periodically. Consider keeping:
- Recent logs (last 30 days)
- Logs from major milestones

## 🔗 Related Documentation

- [Output Format Specification](../rules/output-format.md)
- [Master Workflow](../../.github/instructions/master-workflow.md)

---

**Note**: This README is tracked in git to ensure the folder exists. Actual log files may be gitignored.
