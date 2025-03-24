from llm.base import BaseLLM

class OpenAILLM(BaseLLM):
    def invoke(self, question: str) -> str:
        # Call the OpenAI API using self.url and other parameters.
        return f"OpenAI: Answering '{question}' using model {self.model}"
