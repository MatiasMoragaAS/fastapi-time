# FastAPI Chile Time ⏰

Linter y Pytest![Main Workflow](https://github.com/MatiasMoragaAS/fastapi-time/actions/workflows/main.yml/badge.svg)


Proyecto académico con **FastAPI** y **Docker** que expone un endpoint para obtener la hora oficial de Chile.  
Incluye integración con **GitHub Actions** para CI/CD: linting, tests y despliegue automático de la imagen en Docker Hub.

---

## 🚀 Características
- API construida con **FastAPI**.
- Endpoint `/time` que devuelve la hora local de Chile en formato `YYYY-MM-DD HH:MM:SS`.
- Imagen Docker.
- Workflow de GitHub Actions con:
  - Linting (`flake8`)
  - Tests (`pytest`)
  - Build y push automático a Docker Hub

---

## 📦 Instalación local

1. Clonar el repositorio:
```
   git clone https://github.com/MatiasMoragaAS/fastapi-time.git
   cd fastapi-time
```
2.Instalar dependencias con uv:
```
uv sync
```
3.Ejecutar la aplicación:
```
uv run uvicorn main:app --reload
```
4.Abrir en el navegador:
```
http://localhost:8000/time
```

## 🐳 Usar con Docker
1.Construir la imagen localmente
```
docker build -t matias654/fastapi-time:latest .
```
2.Ejecutar el contenedor
```
docker run -p 8000:8000 matias654/fastapi-time:latest
```
3.Abrir en el navegador:
```
http://localhost:8000/time
```
4.Descargar la imagen desde Docker Hub
```
docker pull matias654/fastapi-time:latest
docker run -p 8000:8000 matias654/fastapi-time:latest
```
## 🧪 Tests

Ejecutar pruebas con:
```
uv run pytest
```
## ⚙️ CI/CD

El repositorio incluye un workflow en .github/workflows/main.yml que:
-Se ejecuta en cada push a main.
-Corre linting y tests.
-Construye y publica la imagen en Docker Hub.
