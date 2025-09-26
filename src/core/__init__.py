"""
Módulo Core - Componentes fundamentales del framework de testing
"""

from src.core.logger import TestLogger, logger
from src.core.assertions import Assertions

__all__ = [
    'TestLogger',
    'logger',
    'Assertions'
]

# Configuración inicial del logger
logger.info("Módulo Core inicializado correctamente")