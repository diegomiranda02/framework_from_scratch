import json
from workflows.rag import RAGWorkflow

class WorkflowBuilder:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.engine = config.get("engine")
        self.workflow_type = config.get("workflow_type")
        self.description = config.get("description")
        self.prompts = config.get("prompts", [])
        self.llm_settings = config.get("llm_settings", [])
        self.attributes = config.get("additional_attributes", {})

    def build(self):
        if self.workflow_type == "simple_rag":
            return RAGWorkflow(self.engine, self.workflow_type, self.description, self.prompts, self.llm_settings,  **self.attributes)
        else:
            raise ValueError(f"Unknown workflow type: {self.workflow_type}")
