# Security Checklist for Gardening App

This checklist ensures secure-by-default practices are followed throughout development. This document integrates with the [CodeGuard](https://github.com/project-codeguard) security framework and should be referenced during all development phases.

---

## Table of Contents

1. [Authentication & Authorization](#authentication--authorization)
2. [Input Validation & Sanitization](#input-validation--sanitization)
3. [Cryptography & Secrets Management](#cryptography--secrets-management)
4. [Database Security](#database-security)
5. [API Security](#api-security)
6. [Session Management](#session-management)
7. [Django-Specific Security](#django-specific-security)
8. [Data Protection & Privacy](#data-protection--privacy)
9. [Infrastructure & Deployment](#infrastructure--deployment)
10. [Supply Chain Security](#supply-chain-security)
11. [Monitoring & Logging](#monitoring--logging)

---

## Authentication & Authorization

### Authentication

- [ ] **Multi-Factor Authentication (MFA)** - Implement MFA for admin and community lead accounts
- [ ] **Password Policies** - Enforce minimum password length (12+ characters), complexity requirements
- [ ] **Password Storage** - Use Django's built-in password hashing (PBKDF2 with SHA256)
- [ ] **Account Lockout** - Implement rate limiting on login attempts (e.g., django-axes or django-ratelimit)
- [ ] **Password Reset Flow** - Secure password reset with time-limited tokens, email verification
- [ ] **Session Timeout** - Configure appropriate session timeouts for different user roles
- [ ] **OAuth/OIDC** - If implementing social auth, use established libraries (django-allauth)

### Authorization

- [ ] **Role-Based Access Control (RBAC)** - Define clear roles: System User, Admin, Community Lead, Community Member, Apprentice, Supporter
- [ ] **Permission Checks** - Verify permissions at both view and model levels
- [ ] **Principle of Least Privilege** - Users should only have access to resources they need
- [ ] **Object-Level Permissions** - Community leads can only manage their own community gardens
- [ ] **Admin Panel Access** - Restrict Django admin to superuser/staff only
- [ ] **API Authorization** - Implement token-based auth (Django REST framework tokens or JWT)

**CodeGuard Reference:** Authentication domain, Authorization domain

---

## Input Validation & Sanitization

### SQL Injection Prevention

- [x] **Use Django ORM** - Prefer ORM queries over raw SQL
- [x] **Parameterized Queries** - If raw SQL is necessary, always use parameterized queries
- [x] **Table Name Validation** - Validate table names against database schema (implemented in `main.py`)
- [x] **No String Interpolation** - Never use f-strings or `.format()` for SQL queries

### Cross-Site Scripting (XSS) Prevention

- [ ] **Template Auto-Escaping** - Ensure Django templates have auto-escaping enabled (default)
- [ ] **User-Generated Content** - Sanitize all user-generated content (plant names, descriptions, feedback)
- [ ] **Content Security Policy (CSP)** - Implement CSP headers via django-csp
- [ ] **Safe Template Filters** - Avoid `|safe` filter unless absolutely necessary

### Command Injection Prevention

- [ ] **Avoid Shell Commands** - Don't use `os.system()`, `subprocess.shell=True`
- [ ] **Input Validation** - Validate file paths, filenames before file operations
- [ ] **Weather API Integration** - Validate/sanitize location data before API calls

### File Upload Security

- [ ] **File Type Validation** - Validate file extensions AND MIME types for plant photos
- [ ] **File Size Limits** - Enforce maximum file size limits
- [ ] **Virus Scanning** - Consider integrating virus scanning for uploads (ClamAV)
- [ ] **Separate Storage** - Store uploads outside webroot, serve via CDN or protected views
- [ ] **Filename Sanitization** - Sanitize uploaded filenames to prevent path traversal

### General Input Validation

- [ ] **Whitelist Validation** - Validate USDA zones (1a-13b), plant types, exposure types
- [ ] **Data Type Validation** - Use Django forms/serializers for validation
- [ ] **Numeric Bounds** - Validate ranges (germination days, spacing, height, etc.)
- [ ] **Email Validation** - Use Django's EmailField
- [ ] **URL Validation** - Use Django's URLField for plant resource links

**CodeGuard Reference:** Input validation domain

---

## Cryptography & Secrets Management

### Secrets Management

- [x] **Environment Variables** - Store secrets in environment variables (DJANGO_SECRET_KEY)
- [x] **Never Commit Secrets** - Ensure `.env` is in `.gitignore`
- [x] **Provide .env.example** - Include `.env.example` with placeholder values
- [ ] **Production Secrets** - Use secret management service (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault)
- [ ] **API Keys** - Store third-party API keys (weather, maps) in environment variables
- [ ] **Rotate Secrets** - Implement secret rotation policy for production

### Django SECRET_KEY

- [x] **Environment Variable** - Load from DJANGO_SECRET_KEY environment variable
- [x] **Development Fallback** - Provide safe fallback for development with warning
- [x] **Production Validation** - Fail fast if SECRET_KEY not set in production
- [ ] **Key Rotation** - Plan for SECRET_KEY rotation without invalidating sessions

### Cryptographic Operations

- [ ] **Use Strong Algorithms** - Use AES-256 for encryption, SHA-256+ for hashing
- [ ] **TLS/SSL Certificates** - Enforce HTTPS in production, use Let's Encrypt or CA-issued certs
- [ ] **Certificate Validation** - Validate SSL certificates for external API calls
- [ ] **Secure Random** - Use `secrets` module for tokens/random values, not `random`

**CodeGuard Reference:** Cryptography domain

---

## Database Security

### Access Control

- [ ] **Database Credentials** - Store in environment variables, never in code
- [ ] **Principle of Least Privilege** - App database user should have minimal permissions
- [ ] **Read-Only Users** - Consider read-only database users for reporting/analytics
- [ ] **Connection Encryption** - Use SSL/TLS for database connections in production

### Data Integrity

- [ ] **Model Validation** - Use Django model validators for data integrity
- [ ] **Constraints** - Define database constraints (unique, foreign key, check constraints)
- [ ] **Timestamps** - Use auto_now_add and auto_now for created/modified tracking
- [ ] **Soft Deletes** - Consider soft deletes for critical data (add is_deleted flag)

### Migrations

- [ ] **Review Migrations** - Always review auto-generated migrations before applying
- [ ] **Backup Before Migrate** - Backup production database before running migrations
- [ ] **Rollback Plan** - Have rollback plan for failed migrations

### Performance & Security

- [ ] **Prepared Statements** - Django ORM uses prepared statements by default
- [ ] **Index Sensitive Data** - Index fields used in WHERE clauses, but avoid over-indexing
- [ ] **Query Optimization** - Use `select_related()` and `prefetch_related()` to prevent N+1 queries

**CodeGuard Reference:** Input validation domain (SQL injection)

---

## API Security

### Authentication & Authorization

- [ ] **API Authentication** - Use Token authentication or JWT for API endpoints
- [ ] **Rate Limiting** - Implement rate limiting to prevent abuse (django-ratelimit)
- [ ] **CORS Configuration** - Configure CORS properly if exposing API to frontend apps
- [ ] **API Versioning** - Version API endpoints (/api/v1/)

### Input/Output

- [ ] **Validate Payloads** - Use DRF serializers to validate all API inputs
- [ ] **Sanitize Outputs** - Don't expose sensitive data in API responses
- [ ] **Error Messages** - Generic error messages, don't leak stack traces/DB info
- [ ] **Pagination** - Implement pagination to prevent large data dumps

### Weather API Integration

- [ ] **API Key Security** - Store weather API keys in environment variables
- [ ] **Rate Limiting** - Respect API rate limits, implement client-side caching
- [ ] **Input Validation** - Validate location data before making API calls
- [ ] **Error Handling** - Handle API failures gracefully
- [ ] **HTTPS Only** - Ensure all API calls use HTTPS

**CodeGuard Reference:** API security best practices

---

## Session Management

### Session Security

- [ ] **Secure Session Cookies** - Set SESSION_COOKIE_SECURE=True in production (HTTPS only)
- [ ] **HttpOnly Cookies** - Set SESSION_COOKIE_HTTPONLY=True (prevent XSS access)
- [ ] **SameSite Cookies** - Set SESSION_COOKIE_SAMESITE='Lax' or 'Strict'
- [ ] **Session Timeout** - Configure SESSION_COOKIE_AGE (e.g., 2 weeks for regular users, 1 hour for admins)
- [ ] **Session Expiry** - Implement absolute session expiry and idle timeout
- [ ] **Logout Functionality** - Properly clear sessions on logout

### CSRF Protection

- [ ] **CSRF Middleware** - Ensure CsrfViewMiddleware is enabled (Django default)
- [ ] **CSRF Tokens** - Include {% csrf_token %} in all forms
- [ ] **CSRF Cookie Security** - Set CSRF_COOKIE_SECURE=True, CSRF_COOKIE_HTTPONLY=True

**CodeGuard Reference:** Session management best practices

---

## Django-Specific Security

### Settings Configuration

- [x] **SECRET_KEY** - Load from environment variable, never commit to version control
- [x] **DEBUG=False** - Load from environment variable, disable in production
- [ ] **ALLOWED_HOSTS** - Configure allowed hosts for production
- [ ] **SECURE_SSL_REDIRECT** - Redirect HTTP to HTTPS in production
- [ ] **SECURE_HSTS_SECONDS** - Enable HSTS (HTTP Strict Transport Security)
- [ ] **SECURE_BROWSER_XSS_FILTER** - Enable browser XSS filtering
- [ ] **X_FRAME_OPTIONS** - Set to 'DENY' to prevent clickjacking
- [ ] **SECURE_CONTENT_TYPE_NOSNIFF** - Prevent MIME-type sniffing

### Django Security Middleware

- [ ] **SecurityMiddleware** - Ensure SecurityMiddleware is enabled
- [ ] **Session Security** - Configure session security settings
- [ ] **CSRF Protection** - Ensure CSRF middleware is enabled

### Admin Panel Security

- [ ] **Admin URL** - Change default /admin/ URL to something less predictable
- [ ] **Admin Access** - Restrict admin access to superuser/staff only
- [ ] **IP Whitelisting** - Consider IP whitelisting for admin panel
- [ ] **Admin Logging** - Log all admin actions

### Third-Party Packages

- [ ] **Keep Updated** - Regularly update Django and third-party packages
- [ ] **Security Advisories** - Subscribe to Django security mailing list
- [ ] **Dependency Scanning** - Use tools like Safety, pip-audit, or Snyk

**CodeGuard Reference:** Platform security (Django)

---

## Data Protection & Privacy

### Personal Data (PII)

- [ ] **Data Minimization** - Only collect necessary personal data
- [ ] **User Profiles** - Protect user profile data (email, location, preferences)
- [ ] **Community Data** - Protect community member information
- [ ] **Data Retention** - Define and implement data retention policy
- [ ] **Right to Deletion** - Implement user account deletion functionality
- [ ] **Data Export** - Allow users to export their data

### Sensitive Data

- [ ] **Email Addresses** - Protect from enumeration, don't expose in API responses
- [ ] **Location Data** - Protect user location data (USDA zone, coordinates)
- [ ] **Community Plot Info** - Ensure users can only view their own plot data

### Compliance

- [ ] **Privacy Policy** - Create and display privacy policy
- [ ] **Terms of Service** - Create and require acceptance of ToS
- [ ] **GDPR Considerations** - If serving EU users, ensure GDPR compliance
- [ ] **COPPA** - If allowing users under 13, ensure COPPA compliance

**CodeGuard Reference:** Data protection domain

---

## Infrastructure & Deployment

### Production Environment (Render)

- [ ] **HTTPS Enforced** - Ensure HTTPS is enforced on Render
- [ ] **Environment Variables** - Configure all secrets via Render environment variables
- [ ] **Database Backups** - Enable automated database backups
- [ ] **Database Encryption** - Enable encryption at rest for database
- [ ] **Static File Serving** - Serve static files via CDN (Cloudflare, AWS CloudFront)
- [ ] **Media File Storage** - Use S3 or similar for user uploads

### Server Configuration

- [ ] **OS Patches** - Keep server OS updated (managed by Render)
- [ ] **Firewall Rules** - Configure firewall to allow only necessary ports
- [ ] **SSH Access** - Disable SSH password auth, use keys only (if applicable)
- [ ] **Container Security** - If using Docker, scan images for vulnerabilities

### CI/CD Security

- [ ] **Secret Scanning** - Enable secret scanning in GitHub
- [ ] **Dependency Scanning** - Use Dependabot or similar
- [ ] **SAST** - Integrate static analysis (Bandit, Semgrep)
- [ ] **Security Tests** - Include security tests in CI pipeline

**CodeGuard Reference:** Cloud security, Infrastructure security

---

## Supply Chain Security

### Dependency Management

- [ ] **Pin Versions** - Pin exact versions in requirements.txt or pyproject.toml
- [ ] **Lock Files** - Use uv.lock for reproducible builds
- [ ] **Verify Sources** - Only install packages from PyPI or trusted sources
- [ ] **Dependency Audit** - Regularly audit dependencies for vulnerabilities (Safety, pip-audit)
- [ ] **Minimal Dependencies** - Only include necessary dependencies

### Package Integrity

- [ ] **Hash Verification** - Verify package hashes during installation
- [ ] **Signed Releases** - Prefer packages with signed releases
- [ ] **SBOM** - Generate Software Bill of Materials for production releases

### Development Dependencies

- [ ] **Separate Dev Dependencies** - Keep dev dependencies separate (--dev flag)
- [ ] **Remove Dev Deps in Prod** - Don't install dev dependencies in production

**CodeGuard Reference:** Supply chain security domain

---

## Monitoring & Logging

### Application Logging

- [ ] **Security Events** - Log authentication attempts, authorization failures, admin actions
- [ ] **Error Logging** - Use Django logging to capture errors
- [ ] **Sensitive Data** - Never log passwords, API keys, or secrets
- [ ] **Log Rotation** - Implement log rotation to prevent disk space issues
- [ ] **Centralized Logging** - Use logging service (Sentry, Datadog, CloudWatch)

### Security Monitoring

- [ ] **Failed Login Attempts** - Monitor and alert on failed login attempts
- [ ] **Unusual Activity** - Monitor for unusual patterns (mass data access, etc.)
- [ ] **File Integrity** - Monitor critical files for unauthorized changes
- [ ] **Vulnerability Scanning** - Regular vulnerability scans (OWASP ZAP, Nessus)

### Incident Response

- [ ] **Incident Response Plan** - Document incident response procedures
- [ ] **Security Contacts** - Maintain list of security contacts
- [ ] **Breach Notification** - Have process for notifying users of breaches

**CodeGuard Reference:** Monitoring best practices

---

## Pre-Deployment Security Checklist

Before deploying to production, verify:

- [x] **Bandit Scan** - All Bandit findings resolved
- [ ] **Django Check** - Run `python manage.py check --deploy`
- [ ] **SECRET_KEY** - Loaded from environment variable, unique for production
- [ ] **DEBUG=False** - Debug mode disabled
- [ ] **ALLOWED_HOSTS** - Configured with production domain(s)
- [ ] **Database** - Using PostgreSQL (not SQLite) with SSL
- [ ] **Static/Media Files** - Served via CDN, not Django
- [ ] **HTTPS** - SSL certificate configured, HTTP redirects to HTTPS
- [ ] **Security Headers** - All security headers configured
- [ ] **Dependency Audit** - No known vulnerabilities in dependencies
- [ ] **Backups** - Automated backups configured and tested
- [ ] **Monitoring** - Error monitoring (Sentry) and logging configured
- [ ] **Rate Limiting** - API and login rate limiting enabled
- [ ] **Password Policy** - Strong password requirements enforced

---

## Security Testing

### Manual Testing

- [ ] **Authentication Testing** - Test login, logout, password reset flows
- [ ] **Authorization Testing** - Verify role-based access controls
- [ ] **Input Validation** - Test with malicious inputs (SQL injection, XSS payloads)
- [ ] **Session Testing** - Test session timeout, cookie security
- [ ] **API Testing** - Test API authentication, rate limiting, input validation

### Automated Testing

- [ ] **Unit Tests** - Security-focused unit tests (authentication, authorization)
- [ ] **Integration Tests** - End-to-end security tests
- [ ] **SAST** - Static analysis with Bandit, Semgrep
- [ ] **DAST** - Dynamic analysis with OWASP ZAP
- [ ] **Dependency Scanning** - Automated dependency vulnerability scans

---

## Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Project CodeGuard](https://github.com/project-codeguard)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)

---

## Changelog

| Date       | Change                                               |
| ---------- | ---------------------------------------------------- |
| 2025-12-15 | Initial security checklist created                   |
| 2025-12-15 | Resolved Bandit findings (SECRET_KEY, SQL injection) |
