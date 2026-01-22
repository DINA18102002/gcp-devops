from src.main import app

def test_index_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    # Check page title / heading content
    assert b"GCP DevOps Platform" in response.data
    assert b"Cloud Build" in response.data
    assert b"Artifact Registry" in response.data
    assert b"GKE" in response.data
