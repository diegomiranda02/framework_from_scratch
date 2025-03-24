from llm.base import BaseLLM

class BedrockLLM(BaseLLM):
    def invoke(self, question: str) -> str:
        # Call the Bedrock API using self.url and other parameters.
        return f"Bedrock: Answering '{question}' using model {self.model}"
