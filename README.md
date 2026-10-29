## YT Downloader
A simple FastAPI web app to download youtube videos and shorts for free. Just copy paste your video URL and get the highest quality video in one go :D

> [!IMPORTANT]  
> Video quality depends on your internet connection's quality

### Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000.

### Project layout

- `main.py` – FastAPI app and routes (`/`, `/download`)
- `templates/` – Jinja2 HTML templates
- `static/` – shared stylesheet and static pages
- `PrototypeDesignSkills.md` – reusable, stack-agnostic UI prototyping skill (principles, tokens, patterns, checklists), with this app as the worked example

<a href='https://yt-with-ease.onrender.com' align='center'><img width='160px' align='center' src='https://render.com/images/deploy-to-render-button.svg'/></a>
