from enum import Enum

class Endpoints(Enum):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # Posts endpoints
    POSTS = "/posts"
    POST_BY_ID = "/posts/{}"
    POST_COMMENTS = "/posts/{}/comments"
    
    # Users endpoints
    USERS = "/users"
    USER_BY_ID = "/users/{}"
    USER_POSTS = "/users/{}/posts"
    
    # Comments endpoints
    COMMENTS = "/comments"
    COMMENT_BY_ID = "/comments/{}"
    
    # Albums endpoints
    ALBUMS = "/albums"
    ALBUM_BY_ID = "/albums/{}"
    
    # Photos endpoints
    PHOTOS = "/photos"
    PHOTO_BY_ID = "/photos/{}"
    
    # Todos endpoints
    TODOS = "/todos"
    TODO_BY_ID = "/todos/{}"