# server/__init__.py
# Upload this file inside the 'server/' folder in your HuggingFace Space repo.

from .app import app, main

__all__ = ["app", "main"]
