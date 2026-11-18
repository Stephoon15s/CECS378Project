"""Application settings."""

import base64
import os
import secrets

SECRET_KEY = os.getenv("BEACHBOARD_SERCRET_KEY") or secrets.token_hex(32)
_export_key_env = os.getenv("BEACHBOARD_EXPORT_KEY")
EXPORT_KEY = base64.b64decode(_export_key_env) if _export_key_env else secrets.token_bytes(32)
