from builders.workflow_builder import WorkflowBuilder
from engines.base import WorkflowEngine
from engines.crewai import CrewAIWorkflowEngine

# Initialize the workflow builder
builder = WorkflowBuilder()
workflow = (builder.set_type("RAG")
                   .set_description("This is a RAG workflow using CrewAI.")
                   .add_prompt("Initialize")
                   .add_prompt("Process Data")
                   .add_prompt("Finalize")
                   .build())

# Initialize the CrewAI workflow engine
engine = CrewAIWorkflowEngine()
engine.add_workflow(workflow)

# Add agents as needed
# engine.add_agent(some_agent)

# Run all workflows
engine.run_all()
