from generator.prompt import PromptBuilder
import pytest


class TestPromptBuilder:
    def test_build_generate_prompt(self):
        """
        Tests building the 'generate_document' prompt.
        """
        code_snippet = "def example():\n    return 'hello'"

        builder = PromptBuilder("generate_document")
        system_prompt, user_prompt = builder.build(code_snippet=code_snippet, feedback="")

        assert "You are an expert" in system_prompt
        assert "Please generate an SDK document" in user_prompt
        assert code_snippet in user_prompt

    def test_build_evaluate_prompt(self):
        """
        Tests building the 'evaluate_document' prompt.
        """
        doc_content = "This is a generated document."

        builder = PromptBuilder("evaluate_document")
        system_prompt, user_prompt = builder.build(document=doc_content)

        assert "Your task is to evaluate" in system_prompt
        assert "Please evaluate the following SDK document" in user_prompt
        assert doc_content in user_prompt

    def test_build_with_feedback(self):
        """
        Tests if feedback is correctly included in the prompt.
        """
        code_snippet = "def example():\n    return 'hello'"
        feedback_text = "The previous version was too short."

        builder = PromptBuilder("generate_document")
        _, user_prompt = builder.build(code_snippet=code_snippet, feedback=feedback_text)

        assert feedback_text in user_prompt

    def test_file_not_found(self):
        """
        Tests that FileNotFoundError is raised for a non-existent prompt.
        """
        with pytest.raises(FileNotFoundError):
            PromptBuilder("non_existent_prompt")
