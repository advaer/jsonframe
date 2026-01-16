# jsonframe

A small, typed JSON “frame” (envelope) for API responses and messages.

The goal is boring reliability: a consistent outer structure that separates
transport-level metadata from business payload.

## Why

APIs, event handlers, and AI-powered services often reinvent the same response
shape: payload, metadata, errors, tracing. jsonframe formalizes this pattern
without coupling it to a specific framework or transport.

## Install

uv:

    uv add jsonframe

pip:

    pip install jsonframe

## Quick start

    from jsonframe import Frame

    frame = Frame(
        data={"user_id": 123},
        meta={"trace_id": "abc-123"},
    )

    frame.to_dict()
    # {
    #   "data": {"user_id": 123},
    #   "meta": {"trace_id": "abc-123"},
    #   "error": None
    # }

## Design principles

- Explicit separation of payload and metadata
- Minimal surface area
- Typed by default
- Framework-agnostic

## Status

jsonframe is in early development (0.0.x).
The public API may change before 1.0.

## License

MIT
