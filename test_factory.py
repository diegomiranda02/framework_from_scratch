from engines.factory import WorkflowEngineFactory

def main():
    # Example 1: Create a Simple RAG workflow with LangGraph
    simple_rag_engine = WorkflowEngineFactory.get_engine(
        engine_type="langgraph",
        workflow_type="simple_rag"
    )
    
    # Run the Simple RAG workflow
    result = simple_rag_engine.run({"query": "What is machine learning?"})
    print(f"\nResult: {result}\n")
    
    # Example 2: Create an Adaptive RAG workflow with CrewAI
    adaptive_rag_engine = WorkflowEngineFactory.get_engine(
        engine_type="langgraph",
        workflow_type="adaptive_rag"
    )
    
    # Run the Adaptive RAG workflow
    result = adaptive_rag_engine.run({"query": "Explain quantum computing"})
    print(f"\nResult: {result}\n")
    
    # Example 3: Create a Self-Reflective RAG workflow using string parameters
    self_reflective_engine = WorkflowEngineFactory.get_engine(
        engine_type="crewai",
        workflow_type="simple_rag"
    )
    
    # Run the Self-Reflective RAG workflow
    result = self_reflective_engine.run({"query": "How does reinforcement learning work?"})
    print(f"\nResult: {result}\n")

if __name__ == "__main__":
    main()