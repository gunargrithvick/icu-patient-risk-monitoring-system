"""Vercel's root-level FastAPI entrypoint.

Vercel discovers Python Functions from recognized files such as ``api/index.py``.
The application itself remains in the ``src`` package used by local, Docker, and
Streamlit runs.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from icu_monitor.api.main import app  # noqa: E402

__all__ = ["app"]
