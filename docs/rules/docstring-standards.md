# Docstring Standards

**Last Updated**: 2025-11-09

This document defines the docstring format and requirements for all Python code in this project.

## 🎯 Style Guide

This project uses **Google-style docstrings** with type hints in function signatures.

## 📋 Module-Level Docstrings

Every Python file must start with an ABOUTME comment and module docstring:

```python
# ABOUTME: This module handles user authentication and session management.
# ABOUTME: It provides functions for login, logout, and token validation.

"""
User authentication module.

This module provides comprehensive authentication functionality including
login, logout, session management, and token validation. It integrates
with the project's security framework and follows CodeGuard guidelines.

Security:
    References .github/instructions/codeguard-0-authentication-mfa.instructions.md

Example:
    >>> from src.auth import login
    >>> result = login("user@example.com", "password")
    >>> print(result.success)
    True
"""
```

## 📝 Function Docstrings

### Simple Functions

```python
def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b
```

### Complex Functions

```python
def authenticate_user(
    email: str,
    password: str,
    remember_me: bool = False
) -> AuthResult:
    """
    Authenticate user with email and password.

    This function validates user credentials against the database,
    creates a session token, and optionally sets a remember-me cookie.
    All security operations follow CodeGuard authentication guidelines.

    Args:
        email: User's email address (validated format)
        password: User's password (will be hashed for comparison)
        remember_me: Whether to create a persistent session. Defaults to False.

    Returns:
        AuthResult object containing:
            - success (bool): Whether authentication succeeded
            - token (str | None): Session token if successful
            - error (str | None): Error message if failed

    Raises:
        ValueError: If email format is invalid
        DatabaseError: If database connection fails

    Security:
        - Password is never logged or stored in plaintext
        - Follows codeguard-0-authentication-mfa.instructions.md
        - Implements rate limiting to prevent brute force attacks

    Examples:
        >>> result = authenticate_user("user@example.com", "password123")
        >>> if result.success:
        ...     print(f"Token: {result.token}")
        Token: example_token_string

        >>> result = authenticate_user("invalid@email", "wrong")
        >>> print(result.error)
        Invalid credentials

    Note:
        This function should only be called over HTTPS in production.
        MFA verification is required for privileged accounts.
    """
    # Implementation here
    pass
```

### Functions with Type Hints

```python
from typing import List, Dict, Optional

def process_data(
    data: List[Dict[str, any]],
    filter_func: Optional[callable] = None
) -> List[Dict[str, any]]:
    """
    Process and optionally filter a list of data dictionaries.

    Args:
        data: List of dictionaries to process
        filter_func: Optional function to filter results.
            Should accept a dict and return bool.

    Returns:
        Processed (and optionally filtered) list of dictionaries

    Examples:
        >>> data = [{"id": 1, "value": "a"}, {"id": 2, "value": "b"}]
        >>> result = process_data(data)
        >>> len(result)
        2

        >>> result = process_data(data, lambda x: x["id"] > 1)
        >>> len(result)
        1
    """
    pass
```

## 🏛️ Class Docstrings

```python
class UserSession:
    """
    Manages user session state and authentication tokens.

    This class handles session creation, validation, and cleanup.
    It integrates with the authentication system and follows
    secure session management practices per CodeGuard guidelines.

    Attributes:
        user_id: Unique identifier for the user
        token: JWT session token
        created_at: Timestamp when session was created
        expires_at: Timestamp when session expires
        is_active: Whether the session is currently active

    Security:
        - Sessions auto-expire after configured timeout
        - Tokens are regenerated on privilege escalation
        - Follows codeguard-0-session-management-and-cookies.instructions.md

    Example:
        >>> session = UserSession(user_id=123)
        >>> session.create_token()
        >>> print(session.is_active)
        True
        >>> session.invalidate()
        >>> print(session.is_active)
        False
    """

    def __init__(self, user_id: int):
        """
        Initialize a new user session.

        Args:
            user_id: Unique identifier for the user

        Raises:
            ValueError: If user_id is not a positive integer
        """
        pass

    def create_token(self, duration: int = 3600) -> str:
        """
        Create a new session token.

        Args:
            duration: Token lifetime in seconds. Defaults to 3600 (1 hour).

        Returns:
            JWT token string

        Raises:
            TokenGenerationError: If token creation fails
        """
        pass
```

## ✅ Requirements Checklist

- [ ] Every module has ABOUTME comment (2 lines)
- [ ] Every module has module-level docstring
- [ ] Every public function/method has docstring
- [ ] Every class has docstring
- [ ] Args section lists all parameters
- [ ] Returns section describes return value
- [ ] Raises section lists exceptions (if any)
- [ ] Examples provided for complex functions
- [ ] Security section for security-sensitive code
- [ ] CodeGuard references where applicable
- [ ] Type hints in function signatures (not in docstring)

## 🚫 Don't Do This

```python
# ❌ Bad: No docstring
def process(data):
    return data

# ❌ Bad: Vague docstring
def authenticate(user, pwd):
    """Authenticates user."""
    pass

# ❌ Bad: Type hints in docstring instead of signature
def add(a, b):
    """
    Add two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum
    """
    return a + b

# ❌ Bad: Missing ABOUTME comment at module level
"""Module for authentication."""  # Should have ABOUTME first
```

## ✅ Do This

```python
# ✅ Good: Complete docstring with examples
def authenticate(email: str, password: str) -> AuthResult:
    """
    Authenticate user with email and password.

    Args:
        email: User's email address
        password: User's password (will be hashed)

    Returns:
        AuthResult with success status and token

    Security:
        Follows codeguard-0-authentication-mfa.instructions.md

    Examples:
        >>> result = authenticate("user@example.com", "pass123")
        >>> result.success
        True
    """
    pass
```

## 🔗 Related Documentation

- [TDD Workflow](../../.github/instructions/tdd-workflow.instructions.md)
- [Master Workflow](../../.github/instructions/master-workflow.md)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

---

**TODO**: Customize this standard based on team preferences and project needs
