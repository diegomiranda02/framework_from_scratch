from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Workflow(ABC):
    def __init__(
        self, 
        engine: str, 
        workflow_type: str, 
        description: str, 
        prompts: List[Dict[str, Any]], 
        llm_settings: Dict[str, Any],
        **kwargs: Dict[str, Any]
    ):
        self.engine = engine
        self.workflow_type = workflow_type
        self.description = description
        self.prompts = prompts
        self.llm_settings = llm_settings
        self.kwargs = kwargs

    @abstractmethod
    def execute_step(self, step_index: int, query: str):
        """
        Execute a specific step in the workflow.
        Must be implemented by subclasses.
        """
        pass