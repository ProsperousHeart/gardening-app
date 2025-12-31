## Threat Modeling

This phase identifies security risks and vulnerabilities using STRIDE framework before implementation, enabling secure-by-design development.

### Purpose

Threat modeling systematically identifies security threats by analyzing:

- System architecture and components
- Data flows and trust boundaries
- Attack surface and entry points
- Potential vulnerabilities and risks
- Mitigation strategies

### Why Threat Modeling Comes AFTER Specifications

**CRITICAL**: Threat modeling must occur AFTER specifications and architecture diagrams because you need to know:

1. **System Architecture**: What components exist and how they interact
2. **Data Flows**: Where data enters, flows through, and exits the system
3. **Trust Boundaries**: What crosses security zones (user input, external APIs, etc.)
4. **Technical Approach**: What technologies, frameworks, and patterns are used
5. **Integration Points**: How the system connects to external services

**Correct Order:**

```
Requirements → Specifications → Architecture Diagrams → Threat Models → Implementation
```

Without specifications, you're guessing at threats. With specifications, you're identifying real risks based on actual system design.

### The STRIDE Framework

This project uses Microsoft's STRIDE framework to categorize threats:

| Category | Threat Type | What It Targets | Example |
|----------|-------------|-----------------|---------|
| **S** | **Spoofing** | Authentication | Attacker impersonates legitimate user |
| **T** | **Tampering** | Integrity | Attacker modifies data in transit or storage |
| **R** | **Repudiation** | Non-repudiation | User denies performing action (no audit trail) |
| **I** | **Information Disclosure** | Confidentiality | Sensitive data exposed to unauthorized parties |
| **D** | **Denial of Service** | Availability | System becomes unavailable to legitimate users |
| **E** | **Elevation of Privilege** | Authorization | Attacker gains higher privileges than allowed |

### The `/create-threat-model` Command

**Format:**

```bash
/create-threat-model <spec-file> [scope]
```

**Examples:**

```bash
# Feature-specific threat model (default)
/create-threat-model docs/specifications/spec_GenUser_plant-search.md

# System-wide threat model
/create-threat-model docs/specifications/spec_sysadmin_user-auth.md high-level-aggregate

# Module-level threat model
/create-threat-model docs/specifications/spec_api_endpoints.md grouped-by-feature
```

### Threat Model Scopes

The scope parameter controls the granularity and focus of threat analysis:

#### `per-requirement` (Default)

- **Focus**: Individual feature or component
- **Use Case**: Analyzing specific functionality (e.g., plant search, user login)
- **Output**: Detailed threats for single feature
- **Example**: Threats specific to plant search API endpoint

#### `high-level-aggregate`

- **Focus**: Entire system or application
- **Use Case**: Understanding overall security posture
- **Output**: Cross-cutting concerns, system-wide threats
- **Example**: Authentication strategy across all features

#### `grouped-by-feature`

- **Focus**: Related features or module
- **Use Case**: Analyzing cohesive group of features
- **Output**: Module-level threats and shared mitigations
- **Example**: All admin panel features together

### What This Command Does

#### Step 1: Analyze Specification and Architecture

- Reads technical specification
- Reviews architecture diagram
- Identifies system components
- Maps data flows
- Identifies trust boundaries

#### Step 2: Apply STRIDE Framework

For each component and data flow, asks:

- **Spoofing**: Can someone impersonate this identity?
- **Tampering**: Can data be modified maliciously?
- **Repudiation**: Can actions be denied?
- **Information Disclosure**: Can sensitive data leak?
- **Denial of Service**: Can the system be made unavailable?
- **Elevation of Privilege**: Can users gain unauthorized access?

#### Step 3: Identify CodeGuard Rules

Maps each threat to relevant CodeGuard security instruction files:

- **Cryptography**: Secure algorithms, key management
- **Input Validation**: SQL injection, XSS, command injection prevention
- **Authentication**: MFA, OAuth/OIDC, session management
- **Authorization**: RBAC/ABAC, access control
- **API Security**: Rate limiting, input validation
- **Data Protection**: Encryption at rest and in transit

Example mapping:

```
Threat: SQL Injection (Tampering)
├─ CodeGuard Rule: input-validation/sql-injection-prevention.md
├─ Mitigation: Use parameterized queries
└─ Test Requirement: Validate all user inputs
```

#### Step 4: Document Threats and Mitigations

Creates comprehensive threat model document:

- **Assets**: What needs protection (user data, credentials, etc.)
- **Entry Points**: Where data enters system (forms, APIs, file uploads)
- **Trust Boundaries**: Security zone transitions
- **Threats**: Specific risks identified via STRIDE
- **Risk Ratings**: Severity (High/Medium/Low) and likelihood
- **Mitigations**: How to prevent or reduce each threat
- **CodeGuard References**: Which security rules apply

#### Step 5: Save and Update

- Saves to `docs/diagrams/threat-model_{name}.md`
- Updates `docs/SPEC-CROSS-REFERENCE.md`
- Updates `docs/INDEX.md`
- Links threat model to specification and architecture diagram

### Integration with Workflow

Threat model creation is **automatically included** in the `/make-spec-from-req` workflow:

```bash
/make-spec-from-req docs/requirements/GenUser/req_genuser_plant-search.md per-requirement
```

This generates:

1. Specification
2. Architecture diagram
3. **Threat model** ← Automatic
4. Documentation updates

You can also create threat models independently:

```bash
/create-threat-model docs/specifications/spec_GenUser_plant-search.md
```

### CodeGuard Integration

This project uses [Project CodeGuard](https://github.com/project-codeguard) (Cisco open-source) for security guidelines.

**Coverage**: 25+ instruction files across 8 domains:

- Cryptography
- Input validation & injection prevention
- Authentication & MFA
- Authorization & access control
- API & web services security
- Data storage & privacy
- Session management
- Supply chain security

**How It Works:**

1. **Threat Identification**: STRIDE analysis identifies potential threats
2. **CodeGuard Mapping**: Each threat mapped to relevant CodeGuard files
3. **Implementation Guidance**: CodeGuard files provide secure coding patterns
4. **Verification**: Security review validates CodeGuard compliance

### Example Threat Model Output

```markdown
# Threat Model: Plant Search Feature

## Assets

- Plant database (scientific names, growing zones, etc.)
- User search queries (potential PII)
- API response data

## Entry Points

- Search API endpoint (/api/plants/search)
- Query parameters (zone, type, characteristics)

## Trust Boundaries

- User browser → API server
- API server → Database

## Threats (STRIDE)

### Spoofing

None identified (public read-only feature)

### Tampering

**T1: SQL Injection via search parameters**

- **Risk**: HIGH
- **Mitigation**: Use parameterized queries, input validation
- **CodeGuard**: input-validation/sql-injection-prevention.md
- **Test**: Validate query sanitization

### Information Disclosure

**I1: Excessive data exposure in API response**

- **Risk**: MEDIUM
- **Mitigation**: Return only necessary fields, no internal IDs
- **CodeGuard**: api-security/data-exposure-prevention.md
- **Test**: Verify response contains only public data

### Denial of Service

**D1: Uncontrolled search queries**

- **Risk**: MEDIUM
- **Mitigation**: Rate limiting, query complexity limits
- **CodeGuard**: api-security/rate-limiting.md
- **Test**: Verify rate limits enforced
```

### Delegates To

- **Slash Command**: `.claude/commands/create-threat-model.md`
- **Prompt**: `.github/prompts/create-threat-model.prompt.md`
- **Instructions**: `.github/instructions/threat-modeling.instructions.md`
- **Security Checklist**: `.github/instructions/security-checklist.md`

### Related Documentation

- **Threat Modeling Instructions**: `.github/instructions/threat-modeling.instructions.md` (detailed STRIDE guidance)
- **Security Checklist**: `.github/instructions/security-checklist.md`
- **CodeGuard Plugin**: `codeguard-security@project-codeguard`
- **Master Workflow**: `.github/instructions/master-workflow.md` (Stage 4)

### Next Steps After Threat Modeling

1. **Security Review**: Review threats with security expert or team
2. **Prioritize Mitigations**: Determine which threats to address first (HIGH priority)
3. **Update Specification**: Add security requirements from threat model to spec
4. **Proceed to Implementation**: With security requirements clear (**Phase 5: TDD Implementation**)
