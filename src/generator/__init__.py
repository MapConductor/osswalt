import os
from generator.prompt import GeneratePromptBuilder
from generator.caller import LlmCaller

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")


class DocumentGenerator:
    def __init__(self, code_snippet: str):
        self.code_snippet = code_snippet

    def generate(self, prompt: str) -> str:
        prompt = GeneratePromptBuilder().build(self.code_snippet)
        response = LlmCaller().call(prompt)
        return response
