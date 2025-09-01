import logging
from rich.logging import RichHandler

logging.basicConfig(
  level=logging.INFO,
  format="%(message)s",
  handlers=[RichHandler()]
)

logger = logging.getLogger("rich")

logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")


# There is no log working here yet, I may continue this project, but under a new language (rust)