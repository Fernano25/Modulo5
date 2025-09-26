import pytest
from src.core.assertions import Assertions
from src.api.schemas import USER_SCHEMA, POST_SCHEMA
from src.core.logger import logger

class TestUsers:
    """Test cases para endpoints de Users"""
    
    def test_get_all_users(self, api_client):
        """Test para obtener todos los usuarios"""
        logger.info("Starting test: Get all users")
        
        response = api_client.get_all_users()
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, {
            "type": "array",
            "items": USER_SCHEMA
        })
        Assertions.assert_list_length(response, 10)  # JSONPlaceholder tiene 10 usuarios
        
        logger.info("Test completed: Get all users")
    
    def test_get_user_by_id(self, api_client):
        """Test para obtener un usuario específico por ID"""
        logger.info("Starting test: Get user by ID")
        
        response = api_client.get_user_by_id(1)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, USER_SCHEMA)
        Assertions.assert_value_equals(response, 'id', 1)
        
        logger.info("Test completed: Get user by ID")
    
    def test_get_user_posts(self, api_client):
        """Test para obtener posts de un usuario específico"""
        logger.info("Starting test: Get user posts")
        
        response = api_client.get_user_posts(1)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, {
            "type": "array",
            "items": POST_SCHEMA
        })
        
        # Verificar que todos los posts pertenecen al usuario correcto
        posts = response.json()
        for post in posts:
            assert post['userId'] == 1, f"Post userId mismatch: {post['userId']}"
        
        logger.info("Test completed: Get user posts")