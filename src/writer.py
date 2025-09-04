from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)


class ContentWriter:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def write(self, content: str, filename: str):
        """
        Writes the given content to a file in the output directory.
        """
        output_path = self.output_dir / filename
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Successfully wrote content to {output_path}")
        except IOError as e:
            logger.error(f"Failed to write to file {output_path}: {e}")
