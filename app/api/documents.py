from fastapi import APIRouter, UploadFile
from app.services.ingest import extract_text

router = APIRouter()

docs = []

@router.post("/upload")
async def upload(file: UploadFile):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text(path)
    docs.append(text)

    return {"status": "uploaded", "length": len(text)}
