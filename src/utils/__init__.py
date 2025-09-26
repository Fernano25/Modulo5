"""
Módulo Utils - Utilidades y helpers para el proyecto de testing
"""

from src.utils.data_generator import DataGenerator
from src.utils.helpers import validate_email, format_response_time

__all__ = [
    'DataGenerator',
    'validate_email',
    'format_response_time'
]

# Inicialización del generador de datos
data_generator = DataGenerator()