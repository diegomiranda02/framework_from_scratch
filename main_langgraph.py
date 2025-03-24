from builders.workflow_builder import WorkflowBuilder
from engines.factory import WorkflowEngineFactory

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

print(f"LANGSMITH_PROJECT: {os.getenv('LANGSMITH_PROJECT')}")
print(f"LANGSMITH_API_KEY: {os.getenv('LANGSMITH_API_KEY')}")

# Initialize the workflow builder
builder = WorkflowBuilder("workflows_config/rag_workflow_config.json")
workflow = builder.build()

print(type(workflow))

# Initialize the workflow engine
simple_rag_engine = WorkflowEngineFactory.get_engine(
        engine_type=workflow.engine,
        workflow_type=workflow.workflow_type
    )

simple_rag_engine.set_workflow(workflow)


# Run the workflow
response = simple_rag_engine.run("Qual a capital da França?")

print(response)
