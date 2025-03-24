from typing import List, Dict, Any

from workflows.base import Workflow

class RAGWorkflow(Workflow):
    def __init__(
        self, 
        engine: str, 
        workflow_type: str, 
        description: str, 
        prompts: List[Dict[str, Any]], 
        llm_settings: Dict[str, Any],
        **kwargs: Dict[str, Any]
    ):
        super().__init__(engine, workflow_type, description, prompts, llm_settings, **kwargs)
        
    def execute_step(self, step_index: int, query: str):
        prompt = self.prompts[step_index]
        prompt_type = prompt.get('type')
        content = prompt.get('content')

        llm = self.llm_settings.get("generation")
        print(llm)

        handler = self._get_prompt_handler(prompt_type)
        if handler:
            handler(content, query)
        else:
            print(f"Unknown prompt type: {prompt_type}")

    def _get_prompt_handler(self, prompt_type: str):
        """
        Map prompt types to their respective handler methods.
        """
        handlers = {
            'system_prompt': self.handle_system_prompt,
            'hallucination_check_prompt': self.handle_hallucination_check_prompt,
            'document_relevancy_prompt': self.handle_document_relevancy_prompt,
        }
        return handlers.get(prompt_type)

    def handle_system_prompt(self, content: str, query: str):
        print(f"Handling system prompt: {content} with query: {query}")
        # Implement system prompt logic here

    def handle_hallucination_check_prompt(self, content: str, query: str):
        print(f"Handling hallucination check prompt: {content} with query: {query}")
        # Implement hallucination check logic here

    def handle_document_relevancy_prompt(self, content: str, query: str):
        print(f"Handling document relevancy prompt: {content} with query: {query}")
        # Implement document relevancy logic here
