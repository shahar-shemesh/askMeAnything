def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the home page!" in response.data  # Replace with actual content
