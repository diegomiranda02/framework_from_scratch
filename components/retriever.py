import requests
import json
from typing import List, Dict, Any
from langsmith import traceable

class Retriever:
    def __init__(self, index_content_sources: List[Dict[str, str]]):
        """
        Initialize the retriever with index content sources.

        index_content_sources: A list of dictionaries each containing an "id" and "url".
        Example:
        [
          {
            "id": "ics_1",
            "url": "https://example.com/doc_chunks_01"
          },
          {
            "id": "ics_2",
            "url": "https://example.com/pdf_upload_42"
          },
          {
            "id": "ics_3",
            "url": "https://example.com/kb_article_17"
          }
        ]
        """
        # Convert list of sources to a dictionary mapping id -> url
        self.api_endpoints = {source["id"]: source["url"] for source in index_content_sources}

    @traceable
    def query_vector_api(self, query_embedding: List[float], top_k: int = 3, api_name: str = "ics_1") -> List[Dict[str, Any]]:
        """Query the specified vector DB API and return documents."""
        if api_name not in self.api_endpoints:
            raise ValueError(f"Unknown API name: {api_name}")

        # Here you would normally query the API using the URL from self.api_endpoints[api_name]
        # For demonstration purposes, we're returning mock responses:
        mock_responses = {
            "ics_1": [
                {"content": "ics_1 Content 1", "source": "ics_1", "link_to_source": "https://example.com/eiffel", "extras_information": {"location": "Paris", "type": "monument"}},
                {"content": "ics_1 Content 2", "source": "ics_1", "link_to_source": "https://example.com/documento_123", "extras_information": {"location": "Documento", "type": "document"}}
            ],
            "ics_2": [
                {"content": "ics_2 Content 1", "source": "ics_2", "link_to_source": "https://example.com/eiffel", "extras_information": {"location": "Paris", "type": "monument"}},
                {"content": "ics_2 Content 2", "source": "ics_2", "link_to_source": "https://example.com/documento_123", "extras_information": {"location": "Documento", "type": "document"}}
            ],
            "ics_3": [
                {"content": "ics_3 Content 1", "source": "ics_3", "link_to_source": "https://example.com/eiffel", "extras_information": {"location": "Paris", "type": "monument"}},
                {"content": "ics_3 Content 2", "source": "ics_3", "link_to_source": "https://example.com/documento_123", "extras_information": {"location": "Documento", "type": "document"}}
            ]
        }

        return mock_responses.get(api_name, [])

    def _format_document(self, doc: Dict[str, Any], index: int) -> str:
        """Format a single document into a human-readable string."""
        formatted = (
            f"Document {index}:\n"
            f"Content: {doc.get('content', '')}\n"
            f"Source: {doc.get('source', '')}\n"
            f"Link: {doc.get('link_to_source', '')}\n"
            f"Extras: {json.dumps(doc.get('extras_information', {}), indent=2)}"
        ).strip()
        return formatted

    def _format_for_llm(self, documents: List[Dict[str, Any]]) -> str:
        """Format documents into a human-readable LLM prompt."""
        formatted_docs = [self._format_document(doc, i) for i, doc in enumerate(documents, 1)]
        return "\n\n".join(formatted_docs)

    def retrieve(self, query_embedding: List[float], top_k: int = 3) -> str:
        """Main interface: queries all APIs and returns a formatted string."""
        all_docs = []
        for api_name in self.api_endpoints:
            all_docs.extend(self.query_vector_api(query_embedding, top_k, api_name))

        return self._format_for_llm(all_docs)
