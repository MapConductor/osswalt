import json
from logging import getLogger
from generator.caller import LlmCaller
from generator.prompt import PromptBuilder

logger = getLogger(__name__)


class DocumentEvaluator:
    def __init__(self):
        self.prompt_builder = PromptBuilder("evaluate_document")
        self.llm_caller = LlmCaller()

    def evaluate(self, document: str) -> tuple[int, str]:
        """
        Uses an LLM to evaluate the generated document and returns a score and feedback.
        """
        system_prompt, user_prompt = self.prompt_builder.build(document=document)

        response_str = self.llm_caller.call(system_prompt, user_prompt)

        try:
            # Clean the response string to ensure it's a valid JSON
            # It often comes wrapped in ```json ... ```
            if response_str.strip().startswith("```json"):
                response_str = response_str.strip()[7:-3].strip()

            response_json = json.loads(response_str)
            score = int(response_json.get("score", 0))
            feedback = response_json.get("feedback", "No feedback provided.")

            logger.info(f"Evaluation Score: {score}")
            logger.info(f"Feedback: {feedback}")
            return score, feedback
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            logger.error(f"Raw response: {response_str}")
            # Return a low score and error message on failure
            return 0, "Failed to get a valid evaluation from the LLM."
