from generator.prompt import GeneratePromptBuilder


class TestGeneratePromptBuilder:
    def test_build_prompt(self):
        code_snippet = "def example():\n    return 'hello'"

        builder = GeneratePromptBuilder()
        system_prompt, user_prompt = builder.build(code_snippet)

        assert system_prompt == ""
        assert "Please generate a sdk document for the following code." in user_prompt
        assert code_snippet in user_prompt
