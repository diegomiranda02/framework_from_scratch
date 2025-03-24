import random

from typing import Literal, Dict, Any, Optional
from typing_extensions import TypedDict, List

from engines.base import WorkflowEngine

from langgraph.graph import StateGraph, START, END

from components.retriever import Retriever
from components.llm import OllamaModel

# Define the state structure
class State(TypedDict):
    question: str
    context: List[str]
    answer: str

class SimpleRagWorkflowEngine(WorkflowEngine):
    def __init__(self):
        self.graph = self.build_graph()
    
    def retrieve(self, state: State) -> dict:
        """Retrieve documents based on the state's question using index content sources."""
        print(f'State question: {state["question"]}')

        # Attempt to get index_content_sources from workflow kwargs
        index_content_sources = self.workflow.kwargs.get('index_content_sources')

        if index_content_sources is None:
            # Raise an exception if index_content_sources is not found
            raise ValueError("index_content_sources not found in kwargs.")
  
        retriever = Retriever(index_content_sources)
        retrieved_docs = retriever.retrieve(state["question"])

        return {"context": retrieved_docs}
    
    # Node: Generation step
    def generate(self, state: State):

        INFERENCE_SERVER = "http://srv-lai-001.tre-rn.jus.br:11434"
        model_name = "mistral-small:24b-instruct-2501-fp16"
        stop = ""
        system_prompt = """
            Você é um agente inteligente projetado para responder perguntas com base em um contexto.
            """

        context = state["context"]
        question = state["question"]

        llm = OllamaModel(
                model=model_name,
                system_prompt=system_prompt,
                temperature=0,
                stop=stop,
                inference_server=INFERENCE_SERVER
            )

        # Call the LLM to generate an answer
        llm_input = f"{system_prompt}\n{context}\n{question}"
        response = llm(llm_input)
        return {"answer": response}
    
    def build_graph(self):
        # Build the sequential flow using LangGraph's StateGraph
        builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        builder.add_edge(START, "retrieve")
        
        return builder.compile()
    
    def run(self, query: str, initial_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run the workflow with the given initial state."""
        if initial_state is None:
            initial_state = {"question": query}
        return self.graph.invoke(initial_state)

    def visualize(self):
        """Return the graph visualization data for external rendering."""
        return self.graph.get_graph()
