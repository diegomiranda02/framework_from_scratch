from engines.crewai.simple_rag import SimpleRAGWorkflowEngine as CrewAISimpleRag
from engines.crewai.adaptive_rag import AdaptiveRAGWorkflowEngine as CrewAdaptiveRag

from engines.langgraph.simple_rag import SimpleRagWorkflowEngine as LangGraphSimpleRag
from engines.langgraph.adaptive_rag import AdaptiveRagWorkflowEngine as LangGraphAdaptiveRag

from typing import Type, Union
from enum import Enum

# Definição dos Enums se ainda não existirem
class EngineType(Enum):
    LANGGRAPH = "langgraph"
    CREWAI = "crewai"

class WorkflowType(Enum):
    SIMPLE_RAG = "simple_rag"
    ADAPTIVE_RAG = "adaptive_rag"


# Factory class to create the appropriate workflow engine
class WorkflowEngineFactory:
    _engine_registry = {
        EngineType.LANGGRAPH: {
            WorkflowType.SIMPLE_RAG: LangGraphSimpleRag,
            WorkflowType.ADAPTIVE_RAG: LangGraphAdaptiveRag
        },
        EngineType.CREWAI: {
            WorkflowType.SIMPLE_RAG: CrewAISimpleRag,
            WorkflowType.ADAPTIVE_RAG: CrewAdaptiveRag
        }
    }
    
    @classmethod
    def get_engine(cls, 
                  engine_type: Union[str, EngineType], 
                  workflow_type: Union[str, WorkflowType],
                  **kwargs) -> Type:
        """
        Create and return a workflow engine based on the specified type.
        
        Args:
            engine_type: The type of engine to use (LangGraph or CrewAI)
            workflow_type: The type of workflow to implement
            **kwargs: Additional parameters to pass to the engine constructor
            
        Returns:
            An instance of the appropriate workflow engine
            
        Raises:
            ValueError: If the specified engine or workflow type is not supported
        """
        # Convert string inputs to enum values if needed
        if isinstance(engine_type, str):
            try:
                engine_type = EngineType(engine_type.lower())
            except ValueError:
                raise ValueError(f"Unsupported engine type: {engine_type}. "
                                f"Supported types: {', '.join([e.value for e in EngineType])}")
        
        if isinstance(workflow_type, str):
            try:
                workflow_type = WorkflowType(workflow_type.lower())
            except ValueError:
                raise ValueError(f"Unsupported workflow type: {workflow_type}. "
                                f"Supported types: {', '.join([w.value for w in WorkflowType])}")
        
        # Get the appropriate engine class
        try:
            engine_class = cls._engine_registry[engine_type][workflow_type]
        except KeyError:
            raise ValueError(f"No implementation found for {engine_type.value} engine with {workflow_type.value} workflow")
        
        # Create and return the engine instance
        return engine_class(**kwargs)
    
    @classmethod
    def register_engine(cls, 
                       engine_type: EngineType, 
                       workflow_type: WorkflowType, 
                       engine_class: Type):
        """Register a new engine implementation for a specific engine and workflow type."""
        if engine_type not in cls._engine_registry:
            cls._engine_registry[engine_type] = {}
        cls._engine_registry[engine_type][workflow_type] = engine_class
