from abc import ABC, abstractmethod
from enum import Enum

# Define an Enum for supported LLM types
class LLMType(Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"
    BEDROCK = "bedrock"
    GOOGLE = "google"
    AZURE = "azure"

# Base class for LLM providers
class BaseLLM(ABC):
    def __init__(self, url: str, model: str, temperature: float, top_k: int, top_p: float):
        self.url = url
        self.model = model
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p

    @abstractmethod
    def invoke(self, question: str) -> str:
        """Invoke the LLM with the given question."""
        pass
