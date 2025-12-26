# Django Secrets Management

This tutorial covers how to securely manage Django secrets and configuration using environment variables instead of hardcoding sensitive values.

## Overview

Secrets like `SECRET_KEY`, database credentials, API keys, and other sensitive configuration should **never** be hardcoded in your Django settings. This tutorial shows you how to use environment variables for local development, GitHub Secrets for CI/CD, and deployment platform variables for production.

**Why environment variables?**

- Prevents accidentally committing secrets to version control
- Different configurations for dev/staging/production
- Easy to rotate secrets without code changes
- Industry standard security practice
- Required for PCI-DSS, SOC 2, and other compliance frameworks

## The Problem

**Bad** - Hardcoded secrets in `settings.py`:

```python
# DON'T DO THIS!
SECRET_KEY = 'django-insecure-hardcoded-key-12345'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'supersecretpassword123',  # NEVER commit this!
        'HOST': 'localhost',
    }
}
```

**Good** - Environment variables in `settings.py`:

```python
# DO THIS INSTEAD
import os
import environ

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
DATABASES = {
    'default': env.db('DATABASE_URL')
}
```

## Setup

### 1. Install django-environ

```bash
# Add django-environ to project dependencies
uv add django-environ
```

### 2. Create `.env` file (Local Development)

Create a `.env` file in your project root (same directory as `manage.py`):

```env
# Django Core Settings
SECRET_KEY=your-local-development-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Email (for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Optional: Third-party API keys
WEATHER_API_KEY=your-weather-api-key
GOOGLE_MAPS_API_KEY=your-maps-api-key
```

**Important:** Add `.env` to `.gitignore` immediately:

```bash
# Add this line to .gitignore
.env
```

### 3. Create `.env.example` (Commit This)

Create `.env.example` as a template for other developers:

```env
# Django Core Settings
SECRET_KEY=changeme
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Optional: Third-party API keys (leave blank if not needed)
WEATHER_API_KEY=
GOOGLE_MAPS_API_KEY=
```

This shows what variables are needed without exposing real secrets.

### 4. Update Django Settings

Modify your `config/settings.py` (or wherever your settings file is):

```python
# ABOUTME: Django settings for gardening application
# ABOUTME: Uses environment variables for configuration

import os
from pathlib import Path
import environ

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environ
env = environ.Env(
    # Set default values and casting
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    SECRET_KEY=(str, ''),
)

# Read .env file (if it exists)
env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

# Email configuration
EMAIL_BACKEND = env(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend'
)

# Optional: Third-party API keys
WEATHER_API_KEY = env('WEATHER_API_KEY', default='')
GOOGLE_MAPS_API_KEY = env('GOOGLE_MAPS_API_KEY', default='')
```

## Usage in Different Environments

### Local Development

**Step 1:** Copy `.env.example` to `.env`

```bash
# Windows
copy .env.example .env

# Unix/macOS
cp .env.example .env
```

**Step 2:** Edit `.env` with your local values

```env
SECRET_KEY=local-development-key-generate-new-one-for-production
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

**Step 3:** Run Django normally

```bash
python manage.py runserver
```

Django automatically loads values from `.env`.

### GitHub Actions (CI/CD)

**Step 1:** Add secrets to GitHub repository

1. Go to your repository on GitHub
2. Navigate to: **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret:
   - Name: `DJANGO_SECRET_KEY`
   - Value: `your-secret-key-for-testing`
5. Repeat for other secrets: `DATABASE_URL`, etc.

**Step 2:** Use secrets in workflow files

Example `.github/workflows/ci.yml`:

```yaml
name: Django CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    env:
      SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
      DEBUG: False
      DATABASE_URL: sqlite:///test_db.sqlite3
      ALLOWED_HOSTS: localhost,127.0.0.1

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install uv
        uses: astral-sh/setup-uv@v4

      - name: Install dependencies
        run: uv sync --all-groups

      - name: Run migrations
        run: python manage.py migrate

      - name: Run tests
        run: python manage.py test
```

### Production (Render)

Since this project deploys to Render:

**Step 1:** Configure environment variables in Render dashboard

1. Go to your service on Render
2. Navigate to **Environment** tab
3. Add environment variables:
   - `SECRET_KEY`: Generate a new secure key (see below)
   - `DEBUG`: `False`
   - `DATABASE_URL`: Automatically provided by Render for PostgreSQL
   - `ALLOWED_HOSTS`: Your Render domain (e.g., `myapp.onrender.com`)
   - Any API keys: `WEATHER_API_KEY`, etc.

**Step 2:** Render automatically injects these into your application

No code changes needed - Django reads from environment variables.

## Generating Secure Secret Keys

**NEVER use the same SECRET_KEY for development and production!**

### Method 1: Django's built-in generator

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Method 2: Python secrets module

```bash
python -c 'import secrets; print(secrets.token_urlsafe(50))'
```

### Method 3: Online generator

Use [Djecrety](https://djecrety.ir/) - Django secret key generator

**Important:** Generate different keys for:
- Local development
- CI/CD testing
- Production

## Common Configuration Patterns

### Database URLs

django-environ supports database URL parsing:

```env
# SQLite
DATABASE_URL=sqlite:///db.sqlite3

# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# PostgreSQL with SSL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname?sslmode=require

# MySQL
DATABASE_URL=mysql://user:password@localhost:3306/dbname
```

### Email Configuration

```env
# Development (console output)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Production (SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

### Boolean Values

django-environ handles boolean conversion:

```env
# All of these evaluate to True
DEBUG=True
DEBUG=true
DEBUG=1
DEBUG=yes
DEBUG=on

# All of these evaluate to False
DEBUG=False
DEBUG=false
DEBUG=0
DEBUG=no
DEBUG=off
DEBUG=
```

### List Values

```env
# Comma-separated values become a list
ALLOWED_HOSTS=localhost,127.0.0.1,myapp.onrender.com

# In Python:
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'myapp.onrender.com']
```

## Best Practices

### 1. Never Commit Secrets

```bash
# Add to .gitignore
.env
.env.local
.env.*.local
*.env
secrets/
```

### 2. Provide .env.example

Always commit `.env.example` with placeholder values so other developers know what variables are needed.

### 3. Use Different Keys per Environment

- **Local development:** Use a simple key like `dev-secret-key-not-for-production`
- **CI/CD:** Use a different key stored in GitHub Secrets
- **Production:** Use a strong, randomly generated key unique to production

### 4. Set DEBUG=False in Production

**ALWAYS** set `DEBUG=False` in production. Debug mode exposes sensitive information in error pages.

```env
# Production .env
DEBUG=False
```

### 5. Rotate Secrets Regularly

- Rotate production `SECRET_KEY` every 90 days
- Rotate API keys according to provider recommendations
- Rotate database passwords quarterly

### 6. Document Required Variables

Keep `.env.example` updated when adding new configuration:

```env
# Add comments explaining what each variable does
# Django secret key for cryptographic signing
SECRET_KEY=changeme

# Enable debug mode (NEVER True in production)
DEBUG=False

# API key for weather data (get from https://weatherapi.com)
WEATHER_API_KEY=
```

## Security Checklist

Before deploying:

- [ ] `.env` is in `.gitignore`
- [ ] `.env.example` is committed (without real values)
- [ ] No secrets are hardcoded in `settings.py`
- [ ] `DEBUG=False` in production environment
- [ ] Production `SECRET_KEY` is different from development
- [ ] Production `SECRET_KEY` is at least 50 characters
- [ ] Database credentials are environment variables
- [ ] All API keys are environment variables
- [ ] `ALLOWED_HOSTS` is properly configured for production domain

## Troubleshooting

### "Environment variable not found"

**Error:**
```
django.core.exceptions.ImproperlyConfigured: Set the SECRET_KEY environment variable
```

**Solution:**
1. Ensure `.env` file exists in project root
2. Verify the variable is defined in `.env`
3. Check you're running commands from the correct directory
4. Make sure `environ.Env.read_env()` is called in `settings.py`

### "SECRET_KEY must not be empty"

**Error:**
```
ValueError: SECRET_KEY must not be empty
```

**Solution:**
```python
# settings.py - Add validation
SECRET_KEY = env('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set")
```

Then set the variable:
```bash
# Generate a new key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Add to .env
SECRET_KEY=generated-key-here
```

### ".env file not being read"

**Solution:**
Verify the path in `settings.py`:

```python
import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env_file = os.path.join(BASE_DIR, '.env')

print(f"Looking for .env at: {env_file}")  # Debug line
print(f"File exists: {os.path.exists(env_file)}")  # Debug line

if os.path.exists(env_file):
    environ.Env.read_env(env_file)
```

### "GitHub Actions tests failing"

**Error:**
```
ImproperlyConfigured: Set the SECRET_KEY environment variable
```

**Solution:**
Ensure workflow file sets environment variables:

```yaml
env:
  SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
  DEBUG: False
```

Or set defaults in `settings.py` for testing:

```python
SECRET_KEY = env('SECRET_KEY', default='test-key-for-ci-only')
```

## What If Secrets Were Committed?

**If you accidentally committed secrets to git:**

1. **Immediately rotate the secret** (generate new SECRET_KEY, reset API keys, change passwords)
2. **Remove from git history** (use `git filter-branch` or BFG Repo-Cleaner)
3. **Force push** (WARNING: coordinate with team first)

**Prevention:**
- Use pre-commit hooks to scan for secrets
- Enable GitHub secret scanning
- Use tools like [detect-secrets](https://github.com/Yelp/detect-secrets)

## Example .env Files

### Development

```env
# .env (local development)
SECRET_KEY=dev-secret-key-not-for-production-12345
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Production

```env
# Production environment variables (Render, Railway, Heroku, etc.)
SECRET_KEY=prod-secure-random-key-50-characters-minimum-abc123xyz789
DEBUG=False
ALLOWED_HOSTS=myapp.onrender.com,www.myapp.com
DATABASE_URL=postgresql://user:pass@host:5432/dbname
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=SG.actual-sendgrid-api-key-here
```

## Additional Resources

- [django-environ Documentation](https://django-environ.readthedocs.io/)
- [Django Settings Best Practices](https://docs.djangoproject.com/en/stable/topics/settings/)
- [The Twelve-Factor App - Config](https://12factor.net/config)
- [GitHub Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Render Environment Variables](https://render.com/docs/environment-variables)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
