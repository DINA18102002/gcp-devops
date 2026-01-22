from src.main import app

def test_index_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to GCP DevOps" in response.data
