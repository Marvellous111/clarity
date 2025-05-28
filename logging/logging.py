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