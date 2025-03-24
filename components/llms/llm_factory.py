from typing import Type, Union
from llm.base import BaseLLM, LLMType
from llm.ollama import OllamaLLM
from llm.openai import OpenAILLM
from llm.bedrock import BedrockLLM
from llm.google import GoogleLLM
from llm.azure import AzureLLM

class LLMFactory:
    _registry = {
        LLMType.OLLAMA: OllamaLLM,
        LLMType.OPENAI: OpenAILLM,
        LLMType.BEDROCK: BedrockLLM,
        LLMType.GOOGLE: GoogleLLM,
        LLMType.AZURE: AzureLLM,
    }
    
    @classmethod
    def get_llm(cls,
                llm_type: Union[str, LLMType],
                url: str,
                model: str,
                temperature: float,
                top_k: int,
                top_p: float) -> BaseLLM:
        """
        Create and return an LLM provider based on the specified type.
        
        Args:
            llm_type: The type of LLM (e.g., "openai", "ollama").
            url: The API endpoint URL.
            model: The model name.
            temperature: The sampling temperature.
            top_k: The top_k parameter.
            top_p: The top_p parameter.
            
        Returns:
            An instance of a subclass of BaseLLM.
            
        Raises:
            ValueError: If the LLM type is unsupported.
        """
        if isinstance(llm_type, str):
            try:
                llm_type = LLMType(llm_type.lower())
            except ValueError:
                supported = ', '.join([t.value for t in LLMType])
                raise ValueError(f"Unsupported LLM type: {llm_type}. Supported types: {supported}")
        try:
            llm_class = cls._registry[llm_type]
        except KeyError:
            raise ValueError(f"No implementation found for LLM type: {llm_type.value}")
        return llm_class(url, model, temperature, top_k, top_p)

    @classmethod
    def register_llm(cls, llm_type: LLMType, llm_class: Type[BaseLLM]):
        """
        Register a new LLM provider implementation.
        
        Args:
            llm_type: The LLM type to register.
            llm_class: The class implementing the LLM provider.
        """
        cls._registry[llm_type] = llm_class
