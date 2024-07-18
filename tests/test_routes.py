import pytest
from app import create_app 
from config import TestingConfig


# Fixture to create a test client for each test
@pytest.fixture
def client():
    app = create_app(TestingConfig)
    with app.test_client() as client:
        yield client
        
        

# Test for successful question processing (201 Created)
def test_ask_valid_question(client):
    payload = {'question': 'What is the capital of France?'}
    response = client.post('/ask', json=payload)
    assert 'answer' in response.get_json()
    assert response.status_code == 201



# Test for handling empty or one word question (400 Bad Request)
def test_ask_empty_question(client):
    payload = {'question': 'hi'}
    response = client.post('/ask', json=payload)

    assert response.status_code == 400
    # Optionally, check for specific error message
    assert 'must contain at least' in response.text



def test_wrong_path(client):
    payload = {'question': 'Who are you?'}
    response = client.post('/', json=payload)
    
    assert response.status_code == 404
    assert 'error_description' in response.get_json()
    assert 'requested URL was not found' in response.text
    
