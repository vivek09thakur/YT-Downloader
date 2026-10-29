import os
from pathlib import Path
from typing import Annotated

import pytube
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="YT Downloader")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/download", response_class=HTMLResponse)
def download_form(request: Request):
    return templates.TemplateResponse(request, "index.html")


# Plain `def` so pytube's blocking download runs in the threadpool, not on the event loop.
@app.post("/download")
def download(request: Request, video_link: Annotated[str, Form()]):
    try:
        stream = pytube.YouTube(video_link).streams.get_highest_resolution()
        file_path = stream.download()
    except Exception:
        return templates.TemplateResponse(request, "error.html")

    return FileResponse(
        file_path,
        media_type="video/mp4",
        filename=os.path.basename(file_path),
    )
