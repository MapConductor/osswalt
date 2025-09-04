import toml
from pathlib import Path
from typing import Tuple


class GeneratePromptBuilder:
    def __init__(self):
        pass

    def build(self, context_code: str) -> Tuple[str, str]:
        current_dir = Path(__file__).parent
        prompt_path = current_dir / "prompt" / "generate_document.toml"

        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_data = toml.load(f)

        system_prompt = ""
        user_prompt_template = prompt_data["messages"][0]["content"][0]["text"]

        user_prompt = user_prompt_template.replace("${context_code}", context_code)

        return system_prompt, user_prompt
