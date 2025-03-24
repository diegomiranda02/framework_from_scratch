from llm.base import BaseLLM

class OllamaLLM(BaseLLM):
    def invoke(self, question: str) -> str:
        # Call the Ollama API using self.url and other parameters.
        return f"Ollama: Answering '{question}' using model {self.model}"
