from engines.langgraph import LangGraphWorkflowEngine

def main():
    try:
        from IPython.display import Image, display
        
        # Create engine
        engine = LangGraphWorkflowEngine()
        
        # Visualize the graph if in IPython environment
        try:
            display(Image(engine.visualize().draw_mermaid_png()))
        except Exception as e:
            print(f"Visualization failed: {e}")
        
        # Run the workflow
        result = engine.run()
        print("Result:", result)
        
    except ImportError:
        print("IPython not available, running without visualization")
        
        # Create and run engine
        engine = LangGraphWorkflowEngine()
        result = engine.run()
        print("Result:", result)

if __name__ == "__main__":
    main()