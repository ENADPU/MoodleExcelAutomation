import pytest
import requests
from get_data import get_user_data, get_course_data

def test_get_user_data_success(requests_mock):
    # Mock de uma resposta da API do Moodle
    user_response = {
        "users": [{"id": 123, "username": "testuser", "fullname": "Test User", "email": "test@example.com"}]
    }
    # Simula a resposta da requisição
    requests_mock.get('https://moodle.example.com', json=user_response)

    user_data = get_user_data(123)
    assert user_data.get('username') == '12345678901'
    assert user_data.get('fullname') == 'Test User'
    assert user_data.get('email') == 'test@example.com'
    assert user_data.get('nome_completo') == 'Test User'

def test_get_user_data_not_found(requests_mock):
    # Simula uma resposta de usuário não encontrado
    user_response = {"users": []}
    requests_mock.get('https://moodle.example.com', json=user_response)

    user_data = get_user_data(999)
    assert user_data == 'Usuário com id=999 não encontrado'

def test_get_course_data_success(requests_mock):
    # Mock de uma resposta da API do Moodle
    course_response = [{"fullname": "Curso Teste"}]
    requests_mock.get('https://moodle.example.com', json=course_response)

    course_name = get_course_data(456)
    assert course_name == 'Curso Teste'
