# jsonframe

A tiny, opinionated helper for **consistent JSON API response frames**.

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
- `meta` contains non-business metadata (optional, always an object)

### Error
```json
{
  "error": {
    "code": "not_found",
    "message": "User not found",
    "details": { ... },
    "trace_id": "..."
  },
  "meta": { ... }
}
```

- Errors are represented by a **single error object**
- HTTP status code communicates severity
- `details` and `meta` are optional

---

## Installation

### Core package
```bash
uv add jsonframe
```

Required dependency:
- `pydantic >= 2.0`

---

### Optional FastAPI integration

FastAPI helpers are **optional** and not installed by default.

```bash
uv add "jsonframe[fastapi]"
```

This installs:
- `fastapi`
- `starlette`

---

## Usage

### Success response
```python
from jsonframe import ok

return ok({"id": 1, "name": "Ada"})
```

### Empty success
```python
from jsonframe import ok

return ok()
```

### List response
```python
from jsonframe import list_ok

return list_ok([{"id": 1}, {"id": 2}])
```

### Paginated list
```python
from jsonframe import paged

return paged(
    items=[{"id": 1}, {"id": 2}],
    total=120,
    limit=20,
    offset=40,
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
from jsonframe import fail

return fail(
    code="validation_error",
    message="Invalid input",
    details={"field": "email"},
)
```

---

## FastAPI helpers (optional)

### Returning framed JSON with status code
```python
from jsonframe.fastapi import json
from jsonframe import ok

return json(ok({"id": 1}), status_code=200)
```

### Raising framed HTTP errors
```python
from jsonframe.fastapi import http_error

raise http_error(
    404,
    code="not_found",
    message="User not found",
    details={"user_id": 42},
)
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
If you can’t explain your API responses by pointing to this README, the library is doing too much.

---

## License

MIT
