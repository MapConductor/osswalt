from unittest.mock import call
from generator import DocumentGenerator


class TestDocumentGenerator:
    def test_generate(self, mocker):
        """
        Tests basic document generation without feedback.
        """
        # Arrange
        mock_llm_caller_class = mocker.patch("generator.LlmCaller")
        mock_llm_instance = mock_llm_caller_class.return_value
        mock_llm_instance.call.return_value = "Mocked LLM Response"

        code_snippet = "def example():\n    return 'hello'"
        generator = DocumentGenerator(code_snippet)

        # Act
        response = generator.generate()

        # Assert
        assert response == "Mocked LLM Response"

        # Check that build was called correctly
        system_prompt, user_prompt = generator.prompt_builder.build(code_snippet=code_snippet, feedback="")
        mock_llm_instance.call.assert_called_once_with(system_prompt, user_prompt)

    def test_generate_with_feedback(self, mocker):
        """
        Tests document generation with feedback.
        """
        # Arrange
        mock_llm_caller_class = mocker.patch("generator.LlmCaller")
        mock_llm_instance = mock_llm_caller_class.return_value
        mock_llm_instance.call.return_value = "Improved Mocked Response"

        code_snippet = "def example():\n    return 'hello'"
        feedback = "The previous document was too generic."
        generator = DocumentGenerator(code_snippet)

        # Act
        response = generator.generate(feedback=feedback)

        # Assert
        assert response == "Improved Mocked Response"

        # Check that build was called with feedback
        feedback_prompt = (
            "\n\n--- PREVIOUS FEEDBACK ---\n"
            "The previous version was not good enough. Please improve the document based on the following feedback:\n"
            f"{feedback}\n"
            "--- END FEEDBACK ---"
        )
        system_prompt, user_prompt = generator.prompt_builder.build(code_snippet=code_snippet, feedback=feedback_prompt)
        mock_llm_instance.call.assert_called_once_with(system_prompt, user_prompt)
