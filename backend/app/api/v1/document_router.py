from fastapi import APIRouter

from ...models.document import Document, DocumentCreate
from ...services.document_service import DocumentService

router = APIRouter()
service = DocumentService()

@router.post("/", response_model=Document)
def create_document(doc_in: DocumentCreate):
    return service.add_document(doc_in)

@router.get("/", response_model=list[Document])
def list_documents():
    return service.list_documents()
