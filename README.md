# jsonframe

[![PyPI version](https://img.shields.io/pypi/v/jsonframe.svg)](https://pypi.org/project/jsonframe/)
[![Python versions](https://img.shields.io/pypi/pyversions/jsonframe.svg)](https://pypi.org/project/jsonframe/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Type-checked with ty](https://img.shields.io/badge/type--checked-ty-blue.svg)](https://github.com/astral-sh/ty)

A tiny, opinionated library for **consistent JSON API response frames**.

`jsonframe` standardizes how APIs return successful responses, collections, pagination metadata, and errors — without dragging in heavy specs or forcing a framework.

---

## Design goals

- Responses are always JSON objects (never top-level arrays)
- Predictable structure across services
- Minimal cognitive load for newcomers
- No `success: true` flags — HTTP status codes already exist
- Small enough to understand in one sitting

---

## Core response rules

### Success
```json
{
  "data": ...,
  "meta": { ... }
}
```

- `data` contains the business payload (object, list, scalar, or `null`)
- `meta` contains non-business metadata (optional, always an object). Typical examples include pagination info, request IDs, timing data, or feature flags — never domain data.

### Error
```json
{
  "detail": "Invalid request payload"
}
```

Or structured:
```json
{
  "detail": {
    "code": "validation_error",
    "message": "Invalid request payload",
    "meta": { ... }
  }
}
```

- Errors are represented by a **single error object** (no arrays, no partial failures)
- HTTP status code communicates severity
- `code` is always present in structured form (value can be `null`)
- `meta` is optional and always an object when present

---

## Examples

#### Example of success payload and framed result
Given the user object and request_id:
```python
from jsonframe import ok

user = {
  "id": 42,
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "role": "admin"
}

result = ok(data=user, meta={"request_id": "req_123"})
```

Result:
```json
{
  "data": {
    "id": 42,
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "role": "admin"
  },
  "meta": {
    "request_id": "req_123"
  }
}
```

#### Example error response (string)
```python
from jsonframe import error

result = error(message="User not found")
```

```json
{
  "detail": "User not found"
}
```

#### Example error response (structured)
```python
from jsonframe import error

result = error(
    code="not_found",
    message="User not found",
    meta={"request_id": "req_123"},
)
```

```json
{
  "detail": {
    "code": "not_found",
    "message": "User not found",
    "meta": {
      "request_id": "req_123"
    }
  }
}
```

---

## Installation

```bash
uv add jsonframe
```

Core dependency:
- `pydantic >= 2.0` (used for lightweight validation and serialization)

---

## Usage

### Success response
```python
from jsonframe import ok

return ok(data={"id": 1, "name": "Ada"})
```

### Empty success
```python
from jsonframe import ok

return ok()
```

### List response
```python
from jsonframe import ok

return ok(data=[{"id": 1}, {"id": 2}])
```

### Paginated list
```python
from jsonframe import ok

return ok(
    data=[{"id": 1}, {"id": 2}],
    meta={"page": {"total": 120, "limit": 20, "offset": 40}},
)
```

Result:
```json
{
  "data": [...],
  "meta": {
    "page": {
      "total": 120,
      "limit": 20,
      "offset": 40
    }
  }
}
```

---

### Error response
```python
from jsonframe import error

return error(
    message="Invalid input",
    code="validation_error",
    meta={"field": "email"},
)
```

---

### Using ErrorDetail with FastAPI
`ErrorDetail` produces the right shape for FastAPI's `HTTPException.detail`:
```python
from fastapi import HTTPException
from jsonframe import ErrorDetail

raise HTTPException(
    status_code=404,
    detail=ErrorDetail(
        message="User not found",
        code="not_found",
        meta={"user_id": 42},
    ).to_dict(),
)
```

FastAPI will return:
```json
{
  "detail": {
    "code": "not_found",
    "message": "User not found",
    "meta": {
      "user_id": 42
    }
  }
}
```

For simple string errors:
```python
raise HTTPException(
    status_code=400,
    detail=ErrorDetail(message="Bad request").to_dict(),
)
```

Returns:
```json
{
  "detail": "Bad request"
}
```

---

## What jsonframe is *not*

- Not a full JSON:API implementation
- Not a validation framework
- Not a transport abstraction
- Not a replacement for OpenAPI or HTTP semantics

---

## When to use jsonframe

- Internal APIs
- BFFs
- Microservices
- AI / LLM-backed services
- Teams that want consistency without ceremony

---

## Philosophy

`jsonframe` is intentionally small.

It standardizes **structure**, not **business logic**.
If you can't explain your API responses by pointing to this README, the library is doing too much.

---

## License

MIT
