import toml
from pathlib import Path
from typing import Tuple, Any


class PromptBuilder:
    def __init__(self, prompt_name: str):
        """
        Initializes the PromptBuilder with a specific prompt file.
        Args:
            prompt_name: The name of the prompt file (without .toml extension).
        """
        current_dir = Path(__file__).parent
        self.prompt_path = current_dir / "prompt" / f"{prompt_name}.toml"
        if not self.prompt_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {self.prompt_path}")

        with open(self.prompt_path, "r", encoding="utf-8") as f:
            self.prompt_data = toml.load(f)["prompt"]

    def build(self, **kwargs: Any) -> Tuple[str, str]:
        """
        Builds the system and user prompts by substituting placeholders.
        Args:
            **kwargs: Keyword arguments to replace placeholders in the prompts.
                      Placeholders should be in the format {{key}}.
        Returns:
            A tuple containing the system prompt and user prompt.
        """
        system_prompt = self.prompt_data.get("system", "")
        user_prompt = self.prompt_data.get("user", "")

        for key, value in kwargs.items():
            system_prompt = system_prompt.replace(f"{{{{{key}}}}}", str(value))
            user_prompt = user_prompt.replace(f"{{{{{key}}}}}", str(value))

        return system_prompt, user_prompt
