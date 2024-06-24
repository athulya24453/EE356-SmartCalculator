from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import time
import json
import os
from main import process_image, calculate_expression, process_image_for_whiteboard, save_bode_plot

app = FastAPI()

host_url = '192.168.1.4'

@app.get("/")
def read_root():
    return {"message": "Routes: /json1 : Image from raspberry pi"}

@app.post("/json1")
async def handle_data(data: dict):
    with open("fromNodeMCU.txt", "w") as f:
        f.write(json.dumps(data))
    return JSONResponse(content=data)

@app.post("/image")
async def image_route(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file part")
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")

    file_path = "img.png"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    result = process_image(file_path)
    try:
        ans = calculate_expression(result)
    except Exception as e:
        ans = [f"Error in processing the image: {str(e)}"]

    # Clean up the file after processing
    os.remove(file_path)

    return {"result": ans}

@app.post("/image_whiteboard")
async def image_route_whiteboard(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file part")
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")

    file_path = "img.png"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    result = process_image_for_whiteboard(file_path)

    # Clean up the file after processing
    os.remove(file_path)

    return {"result": result}

@app.post("/generate_bode_plot")
async def generate_bode_plot(data: dict):
    numerator = data.get('numerator')
    denominator = data.get('denominator')
    path = save_bode_plot(numerator, denominator)  # Call your function to generate and save the Bode plot
    return FileResponse(path, media_type='image/png')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=host_url, port=80)
