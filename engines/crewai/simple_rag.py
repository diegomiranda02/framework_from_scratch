from engines.base import WorkflowEngine

class SimpleRAGWorkflowEngine(WorkflowEngine):
    def __init__(self):
        super().__init__()
        self.agents = []

    def add_agent(self):
        print(f"Running workflow: ")

    def run(self, query: str):
        print(f"Running workflow: {self.workflow.workflow_type}")