# Error Resolution Knowledge Base

**Last Updated**: 2025-11-09

This document catalogs common errors encountered during development and their solutions. It's automatically updated when code self-fixes issues.

## 🎯 Purpose

- Accelerate troubleshooting
- Build institutional knowledge
- Help AI assistants learn from past issues
- Reduce repeated errors

## 📋 How to Use

1. Search for error message or pattern
2. Review context and resolution
3. Apply solution
4. Update KB if you find a new resolution approach

## 🔧 Common Python Errors

### Import Errors

#### ModuleNotFoundError: No module named '{module}'

**Context**: Importing a package that isn't installed

**Error Example**:
```python
import requests
# ModuleNotFoundError: No module named 'requests'
```

**Resolution**:
```bash
# Use uv add (NOT uv pip install)
uv add requests
```

**Prevention**: Always use `uv add` for dependencies, not `uv pip install`

**CodeGuard Reference**: N/A
**Frequency**: Common
**Added**: 2025-11-09

---

### HTTP/Network Errors

#### requests.exceptions.Timeout

**Context**: HTTP request taking too long

**Error Example**:
```python
response = requests.get('https://api.example.com/data')
# requests.exceptions.Timeout: HTTPSConnectionPool(...): Read timed out
```

**Resolution**:
```python
import requests

try:
    response = requests.get(
        'https://api.example.com/data',
        timeout=10  # Set explicit timeout
    )
    response.raise_for_status()
except requests.exceptions.Timeout:
    # Handle timeout appropriately
    logger.error("Request timed out after 10 seconds")
    # Implement retry logic or fail gracefully
except requests.exceptions.RequestException as e:
    # Handle other request errors
    logger.error(f"Request failed: {e}")
```

**Prevention**:
- Always set explicit `timeout` parameter in requests
- Wrap requests in try-except blocks
- Implement retry logic with exponential backoff

**CodeGuard Reference**: `codeguard-0-api-web-services.instructions.md`
**Frequency**: Common
**Added**: 2025-11-09

---

#### requests.exceptions.ConnectionError

**Context**: Unable to establish connection to server

**Error Example**:
```python
response = requests.get('https://unreachable.example.com')
# requests.exceptions.ConnectionError: Failed to establish a new connection
```

**Resolution**:
```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session_with_retries():
    """Create requests session with automatic retry logic."""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

try:
    session = create_session_with_retries()
    response = session.get('https://api.example.com', timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logger.error(f"Connection failed after retries: {e}")
    # Fail gracefully
```

**Prevention**:
- Use session with retry logic
- Set timeout
- Handle ConnectionError explicitly
- Provide user-friendly error messages

**CodeGuard Reference**: `codeguard-0-api-web-services.instructions.md`
**Frequency**: Common
**Added**: 2025-11-09

---

#### requests.exceptions.HTTPError: 403 Forbidden / 401 Unauthorized

**Context**: Permission denied or authentication failed

**Error Example**:
```python
response = requests.get('https://api.example.com/protected')
response.raise_for_status()
# requests.exceptions.HTTPError: 403 Client Error: Forbidden
```

**Resolution**:
```python
import requests
import os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'User-Agent': 'MyApp/1.0'
}

try:
    response = requests.get(
        'https://api.example.com/protected',
        headers=headers,
        timeout=10
    )
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        logger.error("Authentication failed: Invalid or expired token")
    elif e.response.status_code == 403:
        logger.error("Permission denied: Insufficient privileges")
    else:
        logger.error(f"HTTP error occurred: {e}")
```

**Prevention**:
- Store API keys in environment variables (never hardcode)
- Implement proper authentication headers
- Handle 401/403 with specific error messages
- Log authentication failures for security monitoring

**CodeGuard Reference**: `codeguard-1-hardcoded-credentials.instructions.md`, `codeguard-0-authentication-mfa.instructions.md`
**Frequency**: Common
**Added**: 2025-11-09

---

### File Handling Errors

#### FileNotFoundError

**Context**: Attempting to read a file that doesn't exist

**Error Example**:
```python
with open('data.txt', 'r') as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

**Resolution**:
```python
from pathlib import Path

file_path = Path('data.txt')

if not file_path.exists():
    logger.error(f"File not found: {file_path}")
    # Handle missing file appropriately
    # Create default, raise custom exception, etc.
else:
    with open(file_path, 'r') as f:
        content = f.read()
```

**Prevention**:
- Check file existence before operations
- Use pathlib.Path for cross-platform compatibility
- Provide clear error messages
- Consider default file creation

**CodeGuard Reference**: `codeguard-0-file-handling-and-uploads.instructions.md`
**Frequency**: Common
**Added**: 2025-11-09

---

### Database Errors

#### sqlalchemy.exc.IntegrityError

**Context**: Violating database constraints (unique, foreign key, etc.)

**Error Example**:
```python
# Attempting to insert duplicate email
# sqlalchemy.exc.IntegrityError: UNIQUE constraint failed: users.email
```

**Resolution**:
```python
from sqlalchemy.exc import IntegrityError

try:
    user = User(email="user@example.com", password_hash=hash_password(password))
    db.session.add(user)
    db.session.commit()
except IntegrityError as e:
    db.session.rollback()
    logger.warning(f"Database integrity error: {e}")
    # Handle specific constraint violations
    if "UNIQUE constraint" in str(e):
        raise ValueError("User with this email already exists")
    elif "FOREIGN KEY constraint" in str(e):
        raise ValueError("Referenced record does not exist")
    else:
        raise ValueError("Database constraint violation")
```

**Prevention**:
- Check for existing records before insert
- Use proper try-except around database operations
- Always rollback on error
- Provide user-friendly error messages

**CodeGuard Reference**: `codeguard-0-data-storage.instructions.md`
**Frequency**: Common
**Added**: 2025-11-09

---

## 🧪 Testing Errors

### pytest Collection Errors

#### ImportError during test collection

**Context**: Tests can't import source modules

**Resolution**:
```bash
# Ensure proper Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or install package in development mode
uv pip install -e .
```

**Prevention**: Set up proper package structure and imports

**Frequency**: Common
**Added**: 2025-11-09

---

## 🔒 Security Errors

### Cryptography Errors

#### cryptography.fernet.InvalidToken

**Context**: Attempting to decrypt with wrong key or corrupted data

**Resolution**:
```python
from cryptography.fernet import Fernet, InvalidToken

try:
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_data)
except InvalidToken:
    logger.error("Decryption failed: Invalid token or key")
    # Don't expose crypto details to users
    raise ValueError("Unable to decrypt data")
```

**Prevention**:
- Validate encrypted data before decryption
- Use proper key management
- Don't expose crypto errors to end users

**CodeGuard Reference**: `codeguard-0-additional-cryptography.instructions.md`
**Frequency**: Occasional
**Added**: 2025-11-09

---

## 📝 Adding New Entries

When you encounter and resolve a new error:

1. Add a new section with this format:
```markdown
#### {Error Name/Type}

**Context**: {When this error occurs}

**Error Example**:
```
{Code or error message}
```

**Resolution**:
```
{Working solution}
```

**Prevention**: {How to avoid this error}

**CodeGuard Reference**: {Relevant CodeGuard file if applicable}
**Frequency**: {Common | Occasional | Rare}
**Added**: YYYY-MM-DD

---
```

2. Update "Last Updated" at the top of this document
3. Commit the changes

## 🤖 AI Assistant Integration

AI assistants should:
- Reference this KB when encountering known errors
- Add new entries when self-fixing issues
- Update frequency counts when errors recur
- Link to relevant CodeGuard files

---

**TODO**: This KB will grow as the project develops. Organize into categories and consider creating an index if it becomes large.
