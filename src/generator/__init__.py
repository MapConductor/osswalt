import os

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")
