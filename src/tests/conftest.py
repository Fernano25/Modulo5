import pytest
from src.api.client import JSONPlaceholderClient
from src.core.logger import logger
from src.utils.data_generator import DataGenerator

@pytest.fixture(scope="session")
def api_client():
    """Fixture para el cliente API"""
    client = JSONPlaceholderClient()
    logger.info("API Client initialized")
    return client

@pytest.fixture
def data_generator():
    """Fixture para el generador de datos"""
    return DataGenerator()

@pytest.fixture
def setup_test_post(api_client, data_generator):
    """Fixture para setup de test de posts"""
    # Precondiciones: Crear un post de prueba
    post_data = data_generator.generate_post_data(user_id=1)
    response = api_client.create_post(post_data)
    
    # Verificar que se creó correctamente
    assert response.status_code == 201
    created_post = response.json()
    post_id = created_post.get('id')
    
    logger.info(f"Test post created with ID: {post_id}")
    
    yield post_id, created_post
    
    # Postcondiciones: Limpiar el post creado (aunque JSONPlaceholder no persiste cambios)
    logger.info(f"Cleaning up test post ID: {post_id}")

@pytest.fixture
def setup_test_user(api_client):
    """Fixture para setup de test de usuarios"""
    # Obtener un usuario existente para pruebas
    response = api_client.get_user_by_id(1)
    assert response.status_code == 200
    user_data = response.json()
    
    logger.info(f"Using test user ID: {user_data['id']}")
    
    yield user_data