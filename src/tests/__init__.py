"""
Módulo de Tests - Casos de prueba para JSONPlaceholder API
"""

import warnings
import os
import sys

# Asegurar que el path incluye el directorio src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Ignorar warnings específicos durante testing
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Configuración de entorno de testing
TEST_CONFIG = {
    'base_url': 'https://jsonplaceholder.typicode.com',
    'timeout': 30,
    'max_retries': 3
}

__all__ = [
    'TEST_CONFIG'
]

print("Módulo de tests cargado - JSONPlaceholder Test Suite")