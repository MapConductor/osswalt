from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import VertexAI
from langchain_core.output_parsers import StrOutputParser


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
                ("user", "{user_prompt}"),
            ]
        )
        chain = prompt | self.model | StrOutputParser()
        response = chain.invoke({"user_prompt": user_prompt})
        return response
