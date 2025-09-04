import os
import os
from generator.prompt import PromptBuilder
from generator.caller import LlmCaller
from logging import getLogger
from typing import Optional

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

logger = getLogger(__name__)


class DocumentGenerator:
    def __init__(self, code_snippet: str):
        self.code_snippet = code_snippet
        self.prompt_builder = PromptBuilder("generate_document")
        self.llm_caller = LlmCaller()

    def generate(self, feedback: Optional[str] = None) -> str:
        """
        Generates a document, optionally using feedback to improve it.
        """
        prompt_args = {"code_snippet": self.code_snippet, "feedback": ""}
        if feedback:
            feedback_prompt = (
                "\n\n--- PREVIOUS FEEDBACK ---\n"
                "The previous version was not good enough. Please improve the document based on the following feedback:\n"
                f"{feedback}\n"
                "--- END FEEDBACK ---"
            )
            prompt_args["feedback"] = feedback_prompt

        system_prompt, user_prompt = self.prompt_builder.build(**prompt_args)

        logger.debug(f"System Prompt: {system_prompt}\nUser Prompt: {user_prompt}")
        response = self.llm_caller.call(system_prompt, user_prompt)
        return response
