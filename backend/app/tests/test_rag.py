from app.services.rag_service import RagService

rag_service = RagService()

response = rag_service.ask(
    "Where does Lakshay work? What technologies does he use? What projects has he worked on?"
)

print(response)