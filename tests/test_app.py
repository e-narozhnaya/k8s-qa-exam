import pytest
from app import app  # Импортируем Flask-апп

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_status_code(client):
    """Тест проверяет, что главная страница доступна (200 OK)"""
    response = client.get('/')
    assert response.status_code == 200

def test_db_connection_logic():
    """Пример теста логики: проверяем, что приложение вообще пытается стучаться в БД"""
    # проверкa конфигов
    assert app.config['MYSQL_HOST'] == 'mysql-service'
