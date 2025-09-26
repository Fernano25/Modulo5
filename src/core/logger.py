import logging
import sys
from datetime import datetime

class TestLogger:
    def __init__(self, name="JSONPlaceholderTests"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:
            # Formato del log
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # Handler para consola
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            
            # Handler para archivo
            file_handler = logging.FileHandler(f'test_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)
    
    def log_request(self, method, url, headers=None, payload=None):
        self.logger.info(f"Making {method} request to: {url}")
        if headers:
            self.logger.debug(f"Request Headers: {headers}")
        if payload:
            self.logger.debug(f"Request Payload: {payload}")
    
    def log_response(self, status_code, response_data=None):
        self.logger.info(f"Response Status Code: {status_code}")
        if response_data:
            self.logger.debug(f"Response Data: {response_data}")
    
    def info(self, message):
        self.logger.info(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)

# Instancia global del logger
logger = TestLogger()