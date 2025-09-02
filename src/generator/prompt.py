import prompty


class GeneratePromptBuilder:
    def __init__(self):
        pass

    def build(self, context_code: str) -> str:
        inputs = {"context_code": context_code}
        return prompty.execute("prompt/generate_document.prompty", inputs=inputs)
