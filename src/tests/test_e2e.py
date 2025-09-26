import pytest
from src.core.assertions import Assertions
from src.core.logger import logger

class TestEndToEnd:
    """Flujos end-to-end para JSONPlaceholder"""
    
    def test_e2e_post_workflow(self, api_client, data_generator):
        """Flujo E2E completo para gestión de posts"""
        logger.info("Starting E2E test: Post workflow")
        
        # 1. Obtener todos los posts iniciales
        initial_posts = api_client.get_all_posts()
        Assertions.assert_status_code(initial_posts, 200)
        
        # 2. Crear un nuevo post
        new_post_data = data_generator.generate_post_data(
            title="E2E Test Post",
            body="This is an end-to-end test post",
            userId=1
        )
        
        create_response = api_client.create_post(new_post_data)
        Assertions.assert_status_code(create_response, 201)
        created_post = create_response.json()
        post_id = created_post['id']
        
        # 3. Verificar que el post fue creado (simulado)
        get_response = api_client.get_post_by_id(post_id)
        Assertions.assert_status_code(get_response, 200)
        
        # 4. Actualizar el post
        update_data = data_generator.generate_post_data(
            title="Updated E2E Post",
            body="Updated end-to-end test post content",
            userId=1
        )
        update_data['id'] = post_id
        
        update_response = api_client.update_post(post_id, update_data)
        Assertions.assert_status_code(update_response, 200)
        
        # 5. Eliminar el post (simulado)
        delete_response = api_client.delete_post(post_id)
        Assertions.assert_status_code(delete_response, 200)
        
        logger.info("Completed E2E test: Post workflow")
    
    def test_e2e_user_post_interaction(self, api_client, data_generator):
        """Flujo E2E para interacción usuario-post"""
        logger.info("Starting E2E test: User-Post interaction")
        
        # 1. Obtener información de un usuario
        user_response = api_client.get_user_by_id(1)
        Assertions.assert_status_code(user_response, 200)
        user_data = user_response.json()
        
        # 2. Obtener posts del usuario
        user_posts_response = api_client.get_user_posts(1)
        Assertions.assert_status_code(user_posts_response, 200)
        user_posts = user_posts_response.json()
        
        # 3. Verificar que los posts pertenecen al usuario
        for post in user_posts:
            assert post['userId'] == user_data['id']
        
        # 4. Obtener comentarios del primer post del usuario
        if user_posts:
            first_post_id = user_posts[0]['id']
            comments_response = api_client.get_post_comments(first_post_id)
            Assertions.assert_status_code(comments_response, 200)
        
        logger.info("Completed E2E test: User-Post interaction")