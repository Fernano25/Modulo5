import pytest
from src.core.assertions import Assertions
from src.api.schemas import POST_SCHEMA, COMMENT_SCHEMA
from src.core.logger import logger

class TestPosts:
    """Test cases para endpoints de Posts"""
    
    def test_get_all_posts(self, api_client):
        """Test para obtener todos los posts"""
        logger.info("Starting test: Get all posts")
        
        response = api_client.get_all_posts()
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, {
            "type": "array",
            "items": POST_SCHEMA
        })
        Assertions.assert_list_length(response, 100)  # JSONPlaceholder siempre retorna 100 posts
        
        logger.info("Test completed: Get all posts")
    
    def test_get_post_by_id(self, api_client):
        """Test para obtener un post específico por ID"""
        logger.info("Starting test: Get post by ID")
        
        response = api_client.get_post_by_id(1)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, POST_SCHEMA)
        Assertions.assert_value_equals(response, 'id', 1)
        
        logger.info("Test completed: Get post by ID")
    
    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id_parametrized(self, api_client, post_id):
        """Test parametrizado para obtener posts por diferentes IDs"""
        logger.info(f"Starting parametrized test: Get post by ID {post_id}")
        
        response = api_client.get_post_by_id(post_id)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, POST_SCHEMA)
        Assertions.assert_value_equals(response, 'id', post_id)
        
        logger.info(f"Test completed: Get post by ID {post_id}")
    
    def test_create_post(self, api_client, data_generator):
        """Test para crear un nuevo post"""
        logger.info("Starting test: Create new post")
        
        post_data = data_generator.generate_post_data(
            title="Test Post Title",
            body="Test post body content",
            userId=1
        )
        
        response = api_client.create_post(post_data)
        
        Assertions.assert_status_code(response, 201)
        Assertions.assert_json_schema(response, POST_SCHEMA)
        Assertions.assert_value_equals(response, 'title', post_data['title'])
        Assertions.assert_value_equals(response, 'body', post_data['body'])
        Assertions.assert_value_equals(response, 'userId', post_data['userId'])
        
        logger.info("Test completed: Create new post")
    
    def test_update_post(self, api_client, data_generator):
        """Test para actualizar un post existente"""
        logger.info("Starting test: Update post")
        
        update_data = data_generator.generate_post_data(
            title="Updated Post Title",
            body="Updated post body content",
            userId=1
        )
        update_data['id'] = 1  # Forzar ID específico
        
        response = api_client.update_post(1, update_data)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, POST_SCHEMA)
        Assertions.assert_value_equals(response, 'title', update_data['title'])
        Assertions.assert_value_equals(response, 'body', update_data['body'])
        
        logger.info("Test completed: Update post")
    
    def test_delete_post(self, api_client):
        """Test para eliminar un post"""
        logger.info("Starting test: Delete post")
        
        response = api_client.delete_post(1)
        
        Assertions.assert_status_code(response, 200)
        # JSONPlaceholder simula la eliminación pero no persiste cambios
        
        logger.info("Test completed: Delete post")
    
    def test_get_post_comments(self, api_client):
        """Test para obtener comentarios de un post específico"""
        logger.info("Starting test: Get post comments")
        
        response = api_client.get_post_comments(1)
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_schema(response, {
            "type": "array",
            "items": COMMENT_SCHEMA
        })
        
        # Verificar que todos los comentarios pertenecen al post correcto
        comments = response.json()
        for comment in comments:
            assert comment['postId'] == 1, f"Comment postId mismatch: {comment['postId']}"
        
        logger.info("Test completed: Get post comments")