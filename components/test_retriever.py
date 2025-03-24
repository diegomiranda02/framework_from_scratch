from components.retriever import Retriever

api_endpoints = [
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
print(api_endpoints)
retriever = Retriever(api_endpoints)
print(retriever.retrieve("TESTE"))