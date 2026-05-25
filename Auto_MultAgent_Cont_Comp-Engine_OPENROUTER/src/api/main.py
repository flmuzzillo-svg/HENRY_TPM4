from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil
import os

# Add parent to path for importing
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.main import run_contract_analysis

app = FastAPI()

# Mount static folder for the upload form
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "templates"), name="static")

DATA_DIR = Path(__file__).parent.parent / "data" 
TEST_DIR = DATA_DIR / "test_contracts"

# Ensure test_contracts exists
TEST_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = open(Path(__file__).parent / "templates" / "upload.html", "r", encoding="utf-8").read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/process")
async def process_files(
    original: UploadFile = File(...),
    amendment: UploadFile = File(...),
):
    # Save files to TEST_DIR with a unique name
    original_path = TEST_DIR / original.filename
    amendment_path = TEST_DIR / amendment.filename

    # Write original
    with open(original_path, "wb") as f:
        shutil.copyfileobj(original.file, f)
    # Write amendment
    with open(amendment_path, "wb") as f:
        shutil.copyfileobj(amendment.file, f)

    pair_label = original.filename.replace(".pdf", "")  # simple label
    try:
        result = run_contract_analysis(
            original_image_path=original_path,
            amendment_image_path=amendment_path,
            pair_label=pair_label,
        )
    except Exception as exc:
        return JSONResponse(content={"error": str(exc)}, status_code=500)

    return JSONResponse(content=result.model_dump(), status_code=200)
