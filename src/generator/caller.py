from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import VertexAI


class LlmCaller:
    def __init__(self, model_name="gemini-2.5-pro", temperature=0):
        if model_name == "gemini-2.5-pro":
            self.model = VertexAI(model_name=model_name, temperature=temperature)
        else:
            raise ValueError("Unsupported model name")

    def call(self, system_prompt: str, user_prompt: str) -> str:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("user", "{input}"),
            ]
        )
        chain = prompt | self.model
        response = chain.invoke({"input": user_prompt})
        return response
