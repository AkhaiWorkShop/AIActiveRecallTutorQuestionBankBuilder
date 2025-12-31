import io
from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from schemas import EvaluateRequest, EvaluateResponse
from recall.evaluator import evaluate_answer
from recall.presets import PRESETS
from ocr.ocr_engine import run_ocr

router = APIRouter()

@router.post("/evaluate", response_model=EvaluateResponse)
def evaluate(req: EvaluateRequest):
    preset = PRESETS.get(req.preset.upper())
    if not preset:
        raise HTTPException(status_code=400, detail="Invalid preset")

    result = evaluate_answer(
        reference_answer=req.reference_answer,
        reference_concepts=req.reference_concepts,
        student_answer=req.student_answer,
        question_config=preset
    )

    return result
@router.post("/ocr")
async def ocr_endpoint(
    source_id: str = Form(...),
    file: UploadFile = File(...),
    lang: str = Form("ind")
):
    
    # Periksa apakah file dikirim
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided.")
        
    file_content = await file.read()
    file_size = len(file_content)
    
    if file_size == 0:
        raise HTTPException(status_code=400, detail="File is empty.")
    
    file_like_object = io.BytesIO(file_content)

    
    # Jalankan engine OCR kita
    result = run_ocr(file_like_object, lang=lang)
    
    # Jika ada error di engine, kita bisa lempar HTTPException
    if "error" in result:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {result['error']}")
    
    return {
        "source_id": source_id,
        "ocr": {
           "raw_text": result["ocr"]["raw_text"],
            "clean_text": result["ocr"].get("clean_text", "")
        },
        "questions": result["questions"],
        "meta": {
            "avg_confidence": result["meta"]["avg_confidence"],
            "attempt": result["meta"]["attempt"]
        }
    }