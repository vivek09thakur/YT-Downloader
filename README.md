## YT Downloader
A simple FastAPI web app to download youtube videos and shorts for free. Just copy paste your video URL and get the highest quality video in one go :D

Live at [https://yt-with-ease.onrender.com](https://yt-with-ease.onrender.com)

> Video quality depends on your internet connection's quality

### Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000.

### Deploy on Render

[`render.yaml`](render.yaml) is the Render equivalent of `vercel.json` (a [Blueprint](https://render.com/docs/infrastructure-as-code)), and [`.python-version`](.python-version) pins the Python version Render builds with.

For an existing web service created from the Dashboard, update its settings once (Django no longer exists in this repo):

| Setting | Value |
| --- | --- |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

If the service has a `PYTHON_VERSION` environment variable set, remove it (or set it to `3.12.10`) so `.python-version` takes effect.

Alternatively, in the Dashboard choose **New > Blueprint** and connect this repo; because the `name` in `render.yaml` matches the existing service, Render applies the Blueprint to it and keeps it in sync on every push.
