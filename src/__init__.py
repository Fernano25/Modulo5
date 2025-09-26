"""
JSONPlaceholder Test Automation Framework

Framework de automatización de pruebas para JSONPlaceholder API
Desarrollado como proyecto académico de Ingeniería de Sistemas
"""

__version__ = "1.0.0"
__author__ = "Estudiante de Ingeniería de Sistemas"
__status__ = "Development"

# Validación de dependencias
try:
    import requests
    import pytest
    import jsonschema
    import faker
    print("✓ Todas las dependencias están instaladas correctamente")
except ImportError as e:
    print(f"✗ Error de importación: {e}")
    print("Ejecuta: pip install -r requirements.txt")