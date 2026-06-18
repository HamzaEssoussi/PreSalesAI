from fastapi import APIRouter, UploadFile, File, HTTPException
from services.rag_service import RAGService
import uuid
import io

router = APIRouter()
rag = RAGService()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        # Lire le contenu
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")
        
        # Générer un ID unique
        doc_id = str(uuid.uuid4())
        
        # Indexer le document
        rag.index_document(
            doc_id=doc_id,
            content=text,
            metadata={"filename": file.filename}
        )
        
        return {
            "message": "Document indexé avec succès",
            "doc_id": doc_id,
            "chars": len(text)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
async def list_documents():
    info = rag.get_collection_info()
    return {"status": "ok", "count": info["count"]}