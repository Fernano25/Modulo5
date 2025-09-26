# Modulo5 - Proyecto de Recuperacion - Fernando Mollo
# Proyecto de Automatización de Pruebas - JSONPlaceholder API

## Descripción del Producto
JSONPlaceholder es una API REST fake online para testing y prototipado. Proporciona endpoints para recursos comunes como posts, usuarios, comentarios, etc.

## Test Plan

### Objetivos
- Automatizar pruebas de API para JSONPlaceholder
- Validar funcionalidades principales
- Implementar mejores prácticas de testing
- Generar reportes y métricas

### Endpoints a Testear
1. **GET /posts** - Obtener todos los posts
2. **POST /posts** - Crear nuevo post
3. **PUT /posts/{id}** - Actualizar post existente
4. **DELETE /posts/{id}** - Eliminar post

### Estrategia de Testing
- Pruebas unitarias para componentes individuales
- Pruebas de integración para endpoints
- Pruebas end-to-end para flujos completos
- Pruebas de regresión

### Criterios de Aceptación
- Todos los test cases deben pasar
- Cobertura de código > 80%
- Reportes claros y detallados

## Ejecución de Pruebas

### Instalación
```bash
pip install -r requirements.txt
Ejecutar todas las pruebas
bash
python -m pytest src/tests/ -v
Ejecutar por categorías
bash
# Solo pruebas smoke
python -m pytest src/tests/ -m smoke -v

### Solo pruebas E2E
python -m pytest src/tests/ -m e2e -v

# Con cobertura
python -m pytest src/tests/ --cov=src --cov-report=html
Estructura del Proyecto
text
src/
├── api/          # Cliente API y endpoints
├── core/         # Logger y assertions
├── tests/        # Casos de prueba
└── utils/        # Utilidades y generadores
Reportes
Test Report: reports/test_report.html

Coverage Report: reports/coverage/index.html

JUnit Report: reports/junit.xml

Git Actions
El workflow se ejecuta automáticamente en pushes y pull requests a las ramas main y development.

Métricas y Cobertura
Cobertura de código para módulos de posts y usuarios

Reportes HTML interactivos

Métricas de ejecución por tipo de test

Conclusiones
Obstáculos Superados
Configuración inicial de Git Actions

Implementación de logger personalizado

Manejo de schemas JSON complejos

Problemas Resueltos
Reutilización de código mediante fixtures

Parametrización de test cases

Generación de datos aleatorios

Mejoras Futuras
Implementar más flujos E2E

Agregar pruebas de performance

Integrar con más herramientas de CI/CD

text

## 4. Ejecución y Configuración

### Para ejecutar en local:
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/jsonplaceholder-tests.git
cd jsonplaceholder-tests

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas
python -m pytest src/tests/ -v

# Ejecutar con cobertura específica para posts y users
python -m pytest src/tests/test_posts.py src/tests/test_users.py --cov=src.api --cov=src.tests -v
Características Implementadas:
Principio SOLID (S - Single Responsibility)

Logger completo con diferentes niveles

4 endpoints testeados (GET, POST, PUT, DELETE)

Git Actions configurado

Cobertura para features de Posts y Users

2 flujos E2E

Datos aleatorios con Faker

Parametrización de tests

Código mantenible y extensible

Este proyecto demuestra habilidades de ingeniería de software aplicadas a testing automation, siguiendo mejores prácticas y estándares industriales.
