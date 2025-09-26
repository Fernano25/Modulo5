"""
Módulo API - Cliente y configuraciones para JSONPlaceholder API
"""

from src.api.client import JSONPlaceholderClient, APIClient
from src.api.endpoints import Endpoints
from src.api.schemas import POST_SCHEMA, USER_SCHEMA, COMMENT_SCHEMA

__all__ = [
    'JSONPlaceholderClient',
    'APIClient',
    'Endpoints', 
    'POST_SCHEMA',
    'USER_SCHEMA',
    'COMMENT_SCHEMA'
]

# Versión del módulo API
__version__ = "1.0.0"