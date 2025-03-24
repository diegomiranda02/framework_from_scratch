from llm.base import BaseLLM

class AzureLLM(BaseLLM):
    def invoke(self, question: str) -> str:
        # Call the Azure API using self.url and other parameters.
        return f"Azure: Answering '{question}' using model {self.model}"
