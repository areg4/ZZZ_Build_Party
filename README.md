# Backend para la creación automática de Equipos para Zenless Zone Zero

Proyecto de práctica para poner a prueba mis habilidades con Python y FastAPI.

Este proyecto genera equipos para combatir el `END GAME` del juego `ZENLESS ZONE ZERO`.

## Developer Info
 - Gerardo Gudiño García
 - Abril 2026

## Requisitos

- Python 3.9+
- Docker y Docker Compose

## Instalación y Configuración

1. Clona este repositorio:
   ```bash
   git clone
   cd ZZZ_Build_Party
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En Linux/Mac
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Levanta los servicios con Docker:
   ```bash
   docker-compose up --build -d
   ```

## Ejecución

1. Inicia el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

   o con:
   ```bash
   fastapi dev .\app\main.py      
   ```

2. Accede a la documentación interactiva de la API en:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)