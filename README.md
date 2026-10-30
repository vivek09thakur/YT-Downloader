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

### Notes

- Make sure you have a stable internet connection for the best video quality.
- The app downloads the highest quality video available for the given URL.