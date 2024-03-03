import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
import uuid
# uvicorn main:app --host 0.0.0.0 --port 10000

app = FastAPI()

temp_folder = "temp"  # Папка для временного хранения файлов
os.makedirs(temp_folder, exist_ok=True)


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    fname = str(uuid.uuid4())
    file_path = os.path.join(temp_folder, fname)
    with open(file_path, "wb") as file_object:
        file_object.write(file.file.read())

    return {"filename": fname}

@app.get("/download/{file_name}")
async def read_item(file_name: str):
    file_path = os.path.join(temp_folder, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="File not found")

    return FileResponse(file_path)

@app.delete("/delete/{file_name}")
async def delete_item(file_name: str):
    file_path = os.path.join(temp_folder, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="File not found")

    os.remove(file_path)
    return {"message": "File deleted successfully"}


@app.get("/files/all")
async def get_files():
    files = os.listdir(temp_folder)
    return {"files": files}
