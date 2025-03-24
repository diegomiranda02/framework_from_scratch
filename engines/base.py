from workflows.base import Workflow

from abc import ABC, abstractmethod

class WorkflowEngine(ABC):
    def __init__(self):
        self.workflow = None

    def set_workflow(self, workflow):
        self.workflow = workflow

    @abstractmethod
    def run(self, query: str):
        pass

