"""Legacy entry point. Run the unified API from the project root instead:

    uvicorn main:app --reload
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from main import app  # noqa: F401
