import pytest
from app import app  # Импортируем Flask-апп

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

import os

def test_homepage_status_code(client):
    """Тест проверяет, что главная страница доступна (200 OK)"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Successfully connected to the database!' in response.data

def test_homepage_db_failure(client, monkeypatch):
    """Тест проверяет, что главная страница доступна даже если БД лежит"""
    monkeypatch.setitem(app.config, 'MYSQL_PASSWORD', 'wrongpassword')
    response = client.get('/')
    assert response.status_code == 200
    assert b'Failed to connect to the database' in response.data

def test_db_connection_logic():
    """Пример теста логики: проверяем, что приложение применяет конфиги"""
    assert 'MYSQL_HOST' in app.config
    assert 'MYSQL_PASSWORD' in app.config
