import cv2
import numpy as np
import uuid
import os
import requests
import uvicorn
from fastapi import FastAPI, UploadFile, File, Query, HTTPException, BackgroundTasks

app = FastAPI(title="Person Detection API")


tasks = {}

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())



def process_image_task(task_id: str, image_np):

    try:

        boxes, weights = hog.detectMultiScale(image_np, winStride=(8, 8), padding=(8, 8), scale=1.05)
        count = len(boxes)


        for (x, y, w, h) in boxes:
            cv2.rectangle(image_np, (x, y), (x + w, y + h), (0, 255, 0), 2)


        output_filename = f"output_{task_id}.jpg"
        cv2.imwrite(output_filename, image_np)

        tasks[task_id] = {
            "status": "completed",
            "person_count": count,
            "result_image": output_filename
        }
    except Exception as e:
        tasks[task_id] = {"status": "error", "message": str(e)}



@app.get("/status/{task_id}")
async def get_status(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Nie znaleziono zadania")
    return tasks[task_id]



@app.get("/detect/local")
async def detect_local(filename: str, background_tasks: BackgroundTasks):
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="Plik nie istnieje")

    task_id = str(uuid.uuid4())
    image = cv2.imread(filename)

    tasks[task_id] = {"status": "processing"}
    background_tasks.add_task(process_image_task, task_id, image)

    return {"task_id": task_id, "message": "Zadanie (lokalne) w kolejce"}



@app.get("/detect/url")
async def detect_url(background_tasks: BackgroundTasks, url: str = Query(...)):
    task_id = str(uuid.uuid4())

    try:
        resp = requests.get(url)
        nparr = np.frombuffer(resp.content, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception:
        raise HTTPException(status_code=400, detail="Błąd pobierania z URL")

    tasks[task_id] = {"status": "processing"}
    background_tasks.add_task(process_image_task, task_id, image)

    return {"task_id": task_id, "message": "Zadanie (URL) w kolejce"}


@app.post("/detect/upload")
async def detect_upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    task_id = str(uuid.uuid4())

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    tasks[task_id] = {"status": "processing"}
    background_tasks.add_task(process_image_task, task_id, image)

    return {"task_id": task_id, "message": "Zadanie (Upload) w kolejce"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)