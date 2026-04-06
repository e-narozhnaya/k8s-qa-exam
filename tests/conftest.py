import pytest
import os
from app import app  # Импортируем Flask-апп

@pytest.fixture
def client():
    # Поднимаем тестовый клиент
    with app.test_client() as client:
        yield client

@pytest.fixture
def current_env():
    # Читаем то, что я выбрала в интерфейсе GitHub
    env = os.getenv('CHOSEN_ENV', 'local')
    print(f"\n[INFO] Тесты запускаются для окружения: {env}")
    return env
