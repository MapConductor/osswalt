from generator import DocumentGenerator


class TestDocumentGenerator:
    def test_generate(self, mocker):
        # Arrange
        mock_llm_caller = mocker.patch("generator.LlmCaller")
        mock_instance = mock_llm_caller.return_value
        mock_instance.call.return_value = "Mocked LLM Response"

        code_snippet = "def example():\n    return 'hello'"
        generator = DocumentGenerator(code_snippet)

        # Act
        response = generator.generate()

        # Assert
        assert response == "Mocked LLM Response"
        system_prompt, user_prompt = generator.prompt_builder.build(code_snippet)
        mock_instance.call.assert_called_once_with(system_prompt, user_prompt)
