---
title: CodeGuard Integration as per GenAI
description: Claude used to generate this for MVP planning. Still needs to be reviewed as of 20251227 for alignment with original MVP plans.
---

## [CodeGuard Integration](./Code_Guard_Integration.md)

**Plugin**: `codeguard-security@project-codeguard`

**Documentation**: <a href="https://project-codeguard.org/" rel="noopener noreferrer" target=_blank>https://project-codeguard.org/</a>

**Update command**: `/plugin update codeguard-security@project-codeguard`

### Security Coverage Areas

CodeGuard provides security rules across 8 domains. Each requirement file must include security considerations in the **Security Considerations** section:

1. **Cryptography**

    - Relevant for: Account Favorites, Community Member authentication
    - Requirements: Secure password storage (bcrypt/Argon2), HTTPS only, no hardcoded secrets

2. **Input Validation**

    - Relevant for: ALL requirements (especially user input forms)
    - Requirements: Server-side validation, SQL injection prevention, XSS prevention, command injection prevention

3. **Authentication**

    - Relevant for: Account Favorites, all Community Member requirements, Admin requirements
    - Requirements: MFA for admin, OAuth/OIDC for user accounts, secure session management, password requirements

4. **Authorization**

    - Relevant for: Community Member requirements, Admin requirements
    - Requirements: RBAC implementation, principle of least privilege, role inheritance model, permission checks at API and UI layers

5. **Supply Chain Security**

    - Relevant for: ALL requirements (dependency management)
    - Requirements: Dependency scanning, SBOM generation, pinned versions

6. **Cloud Security**

    - Relevant for: Weather API, file uploads, cloud storage
    - Requirements: API key security, rate limiting, secure file storage

7. **Platform Security**

    - Relevant for: ALL requirements
    - Requirements: Security headers, CSRF protection, secure cookies, security.txt

8. **Data Protection**

    - Relevant for: ALL requirements (especially PII)
    - Requirements: Data minimization, encryption at rest/transit, GDPR compliance, privacy controls

### CodeGuard in [Requirements Template](../../templates/requirements-template.md)

The template section **Security Considerations** (lines ~380-395) includes:

```markdown
### Security Considerations

Ensure we are also using CodeGuard rules for security best practices! Including but not limited to:

- **Input Sanitization:** How should user input be sanitized?
- **Authentication:** Does this require authentication? What method?
- **Authorization:** What permissions are required? Role-based access?
- **Data Privacy:** What sensitive data must be protected?
- **Encryption:** At rest? In transit?
- **Vulnerability Mitigation:** SQL injection, XSS, CSRF, command injection, etc.
- **Secret Management:** How are secrets stored and accessed?
- **Audit Logging:** What actions need to be logged?
- **XSS Prevention:** What measures prevent cross-site scripting?
- **CSRF Protection:** Is CSRF protection needed?
- **CodeGuard Rules:** ALWAYS utilize CodeGuard rules for secure coding practices
```

### CodeGuard in Threat Models

Every specification will have an associated threat model (`.github/prompts/create-threat-model.prompt.md`) using **STRIDE methodology**:

- **S**poofing (Authentication)
- **T**ampering (Data Integrity)
- **R**epudiation (Audit Logging)
- **I**nformation Disclosure (Data Privacy)
- **D**enial of Service (Availability)
- **E**levation of Privilege (Authorization)

Threat models will reference CodeGuard rules for mitigation strategies.

### CodeGuard Review Process

After code generation, run:

```
/security-review <module-path>
```

This executes `.github/prompts/security-review.prompt.md` which:
1. Analyzes code against CodeGuard rules
2. Identifies security vulnerabilities
3. Provides remediation recommendations
4. Generates security review report