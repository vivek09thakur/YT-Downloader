from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home_renders_download_form():
    response = client.get("/")
    assert response.status_code == 200
    assert 'name="video_link"' in response.text
    assert '/download" method="post"' in response.text


def test_stylesheet_is_served():
    response = client.get("/static/style.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]


def test_invalid_link_renders_error_page():
    response = client.post("/download", data={"video_link": "not-a-youtube-link"})
    assert response.status_code == 200
    assert "Download Failed" in response.text
