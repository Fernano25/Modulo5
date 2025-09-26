"""
Helpers utilities para el proyecto
"""

import re
from datetime import datetime
from typing import Any, Dict

def validate_email(email: str) -> bool:
    """
    Valida formato de email
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def format_response_time(response_time: float) -> str:
    """
    Formatea el tiempo de respuesta a string legible
    """
    if response_time < 1:
        return f"{response_time * 1000:.2f} ms"
    else:
        return f"{response_time:.2f} s"

def sanitize_test_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitiza datos de prueba removiendo valores None
    """
    return {k: v for k, v in data.items() if v is not None}

def get_timestamp() -> str:
    """
    Retorna timestamp actual formateado
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_percentage(passed: int, total: int) -> float:
    """
    Calcula porcentaje de tests pasados
    """
    if total == 0:
        return 0.0
    return (passed / total) * 100