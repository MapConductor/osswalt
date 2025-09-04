import os
from generator.prompt import GeneratePromptBuilder
from generator.caller import LlmCaller
from logging import getLogger

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

logger = getLogger(__name__)


class DocumentGenerator:
    def __init__(self, code_snippet: str):
        self.code_snippet = code_snippet

    def generate(self) -> str:
        system_prompt, user_prompt = GeneratePromptBuilder().build(self.code_snippet)
        logger.debug(f"System Prompt: {system_prompt}\nUser Prompt: {user_prompt}")
        response = LlmCaller().call(system_prompt, user_prompt)
        return response
