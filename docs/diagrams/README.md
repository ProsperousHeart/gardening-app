# Diagrams

This folder contains visual documentation including architecture diagrams, threat models, sequence diagrams, ERDs, and other technical diagrams.

## 📁 Diagram Types

Diagrams use filename prefixes to indicate type:

- `architecture-{name}.md` - System architecture diagrams
- `threat-model-{name}.md` - Security threat models
- `sequence-{name}.md` - Sequence/interaction diagrams
- `erd-{name}.md` - Entity relationship diagrams (database schemas)
- `component-{name}.md` - Component diagrams
- `deployment-{name}.md` - Deployment/infrastructure diagrams

## 🎨 Format

All diagrams use **Mermaid** syntax embedded in Markdown files for:

- Version control friendly (text-based)
- Renders in GitHub, VSCode, and documentation sites
- Easy to maintain and diff

Optional: Separate `.mmd` files can be created alongside `.md` files for external tool compatibility.

## ♻️ Versioning Strategy

**IMPORTANT**: When updating diagrams, create a new versioned file rather than editing the original.

### Why?

- Preserves history
- Better IDE compatibility (some IDEs don't render changes well)
- Avoids CLI-only edits that users might miss
- Easy rollback if needed

### Naming Convention

**Option 1 - Version numbers**:

```
architecture-auth-v1.md
architecture-auth-v2.md
architecture-auth-v3.md
```

**Option 2 - Dates**:

```
architecture-auth-2025-11-09.md
architecture-auth-2025-12-15.md
```

## 📚 Creating Diagrams

Follow these instruction files:

- [Architecture Diagrams](../../.github/instructions/architecture-diagrams.instructions.md)
- [Threat Modeling](../../.github/instructions/threat-modeling.instructions.md)

## 🔗 Cross-Referencing

All diagrams should be linked in:

- [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)
- Related requirement or specification documents

## 📝 Diagram Template

Each diagram file should include:

```markdown
# {Diagram Type}: {Name}

**Requirement**: [REQ-XXX](../requirements/req-xxx.md)
**Specification**: [SPEC-XXX](../specifications/spec_xxx.md)
**Date**: YYYY-MM-DD
**Version**: v1 (or date)
**Status**: Draft | Under Review | Approved

## Overview

[Description of what this diagram shows]

## Diagram

\`\`\`mermaid
[Mermaid diagram code]
\`\`\`

## Notes

[Any relevant notes, security considerations, or CodeGuard references]

## References

- **Cross-Reference**: [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)
```

## 🤖 AI Assistant Usage

### Generate Architecture Diagram

```
Use the create-architecture-diagram prompt for docs/specifications/spec_auth.md
```

### Generate Threat Model

```
Use the create-threat-model prompt for docs/requirements/req_auth.md with scope per-requirement
```

---

**Template Note**: Start creating diagrams at the requirements stage and maintain them throughout development.
