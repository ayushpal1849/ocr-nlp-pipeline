import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from utils.ocr_engine import OCREngine

app = FastAPI(
    title="OCR & NLP Extraction API",
    description="API to extract structured data from documents using YOLOv8 and Tesseract",
    version="1.0"
)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize OCR Engine
ocr_engine = OCREngine()

@app.get("/")
def home():
    return {"status": "running", "message": "OCR & NLP Pipeline API is Active (FastAPI)"}

@app.post("/api/extract")
async def extract_data(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    # Create file path
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        # Save uploaded file locally
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process the image using our OCR Engine
        # Note: OCREngine is synchronous (CPU bound), so it runs directly here.
        # For extremely heavy loads, we would use background tasks, but this is fine for a demo.
        result = ocr_engine.process_document(file_path)
        
        # Clean up (delete file after processing)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return JSONResponse(content={
            "status": "success",
            "data": result
        })

    except Exception as e:
        # Clean up if error occurs
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))

# Note: In FastAPI, we run the server using 'uvicorn' command in terminal, not by running python app.py directly (though you can configure it).