import requests
from src.core.logger import logger
from src.api.endpoints import Endpoints

class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or Endpoints.BASE_URL.value
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'JSONPlaceholder-Test-Automation/1.0'
        })
    
    def _make_request(self, method, endpoint, **kwargs):
        """Método base para realizar requests HTTP"""
        url = f"{self.base_url}{endpoint}"
        
        # Log request details
        logger.log_request(method, url, self.session.headers, kwargs.get('json'))
        
        response = self.session.request(method, url, **kwargs)
        
        # Log response details
        logger.log_response(response.status_code, response.json() if response.text else None)
        
        return response
    
    def get(self, endpoint, **kwargs):
        return self._make_request('GET', endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self._make_request('POST', endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self._make_request('PUT', endpoint, **kwargs)
    
    def patch(self, endpoint, **kwargs):
        return self._make_request('PATCH', endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        return self._make_request('DELETE', endpoint, **kwargs)

class JSONPlaceholderClient(APIClient):
    """Cliente específico para JSONPlaceholder API"""
    
    def get_all_posts(self):
        return self.get(Endpoints.POSTS.value)
    
    def get_post_by_id(self, post_id):
        return self.get(Endpoints.POST_BY_ID.value.format(post_id))
    
    def create_post(self, post_data):
        return self.post(Endpoints.POSTS.value, json=post_data)
    
    def update_post(self, post_id, post_data):
        return self.put(Endpoints.POST_BY_ID.value.format(post_id), json=post_data)
    
    def delete_post(self, post_id):
        return self.delete(Endpoints.POST_BY_ID.value.format(post_id))
    
    def get_all_users(self):
        return self.get(Endpoints.USERS.value)
    
    def get_user_by_id(self, user_id):
        return self.get(Endpoints.USER_BY_ID.value.format(user_id))
    
    def get_user_posts(self, user_id):
        return self.get(Endpoints.USER_POSTS.value.format(user_id))
    
    def get_post_comments(self, post_id):
        return self.get(Endpoints.POST_COMMENTS.value.format(post_id))