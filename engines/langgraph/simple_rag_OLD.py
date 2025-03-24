import random

from typing import Literal, Dict, Any, Optional
from typing_extensions import TypedDict

from engines.base import WorkflowEngine

from langgraph.graph import StateGraph, START, END

# Define the state structure
class State(TypedDict):
    query: str
    graph_state: str

class SimpleRagWorkflowEngine(WorkflowEngine):
    def __init__(self):
        self.graph = self.build_graph()
    
    def node_1(self, state: State) -> State:
        print("---Node 1---")
        print(self.workflow.workflow_type)
        print(self.workflow.description)
        
        # Initialize variables to store prompt contents
        system_prompt = None
        hallucination_check_prompt = None
        document_relevancy_prompt = None

        # Iterate over the list of prompts
        for prompt in self.workflow.prompts:
            prompt_type = prompt.get('type')
            content = prompt.get('content')
            
            # Assign content to the corresponding variable based on prompt type
            if prompt_type == 'system_prompt':
                system_prompt = content
            elif prompt_type == 'hallucination_check_prompt':
                hallucination_check_prompt = content
            elif prompt_type == 'document_relevancy_prompt':
                document_relevancy_prompt = content

        # Output the assigned variables
        print(f"System Prompt: {system_prompt}")
        print(f"Hallucination Check Prompt: {hallucination_check_prompt}")
        print(f"Document Relevancy Prompt: {document_relevancy_prompt}")

        return {"graph_state": state['graph_state'] + " I am"}
    
    def node_2(self, state: State) -> State:
        print("---Node 2---")
        return {"graph_state": state['graph_state'] + " happy!"}
    
    def node_3(self, state: State) -> State:
        print("---Node 3---")
        return {"graph_state": state['graph_state'] + " sad!"}
    
    def decide_mood(self, state: State) -> Literal["node_2", "node_3"]:
        # Often, we will use state to decide on the next node to visit
        # Here, let's just do a 50/50 split between nodes 2, 3
        if random.random() < 0.5:
            # 50% of the time, we return Node 2
            return "node_2"
        # 50% of the time, we return Node 3
        return "node_3"
    
    def build_graph(self):
        # Build graph
        builder = StateGraph(State)
        builder.add_node("node_1", self.node_1)
        builder.add_node("node_2", self.node_2)
        builder.add_node("node_3", self.node_3)
        
        # Logic
        builder.add_edge(START, "node_1")
        builder.add_conditional_edges("node_1", self.decide_mood)
        builder.add_edge("node_2", END)
        builder.add_edge("node_3", END)
        
        # Compile and return
        return builder.compile()
    
    def run(self, query: str, initial_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run the workflow with the given initial state."""
        if initial_state is None:
            initial_state = {"graph_state": "Hi, this is Lance.", "query": query}
        return self.graph.invoke(initial_state)

    def visualize(self):
        """Return the graph visualization data for external rendering."""
        return self.graph.get_graph()
