# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_register(client):
    """Test registration route."""
    response = client.post('/register', data={'name': 'test_user', 'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200  # Assuming registration succeeds, you might want to check for a different status code here

def test_books(client):
    """Test books route."""
    response = client.get('/books')
    assert response.status_code == 302  # Expecting redirect status code since login is required

def test_issue_book(client):
    """Test issue book route."""
    response = client.get('/list_issue_book')
    assert response.status_code == 302  # Expecting redirect status code since login is required

def test_add_book(client):
    """Test add book route."""
    response = client.post('/save_book', data={'name': 'Test Book', 'isbn': '1234567890', 'no_of_copy': '1', 'category': '1', 'author': '1', 'rack': '1', 'publisher': '1', 'status': 'Available', 'action': 'addBook'})
    assert response.status_code == 302  # Assuming book addition succeeds, you might want to check for a different status code here

def test_save_author(client):
    """Test save author route."""
    response = client.post('/saveAuthor', data={'name': 'Test Author', 'status': 'Active', 'action': 'addAuthor'})
    assert response.status_code == 302  # Assuming author addition succeeds, you might want to check for a different status code here

# Add more test cases for other routes as needed
