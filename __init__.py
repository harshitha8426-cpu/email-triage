"""OpenEnv Server Package

This package provides a FastAPI-based server for the Email Triage environment.
It exposes OpenEnv-compatible reset, step, and state endpoints.
"""

from server.app import app, main

__version__ = "1.0.0"
__all__ = ["app", "main"]
