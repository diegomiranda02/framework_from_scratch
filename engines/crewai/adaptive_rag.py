from engines.base import WorkflowEngine
from crewai import Agent, Crew

class AdaptiveRAGWorkflowEngine(WorkflowEngine):
    def __init__(self):
        super().__init__()
        self.agents = []

    def add_agent(self):
        print(f"Running workflow: ")

    def run(self, query: str):
        print(f"Running workflow: {self.workflow.workflow_type}")