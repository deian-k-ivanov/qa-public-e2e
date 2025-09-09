import os

# Default values (can be overridden via environment variables in GitHub Actions)
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
DEFAULT_BROWSER_NAME = os.getenv("BROWSER", "chromium")

# Default users
STANDARD_USER = "standard_user"
LOCED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"
ERROR_USER = "error_user"
VISUAL_USER = "visual_user"
PASSWORD = "secret_sauce"
