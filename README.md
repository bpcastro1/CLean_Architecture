# Bookstore API

API REST desarrollada con FastAPI siguiendo los principios de Clean Architecture para gestionar una relación 1:N entre Autores y Libros.


## Requisitos

- Python 3.8+
- PostgreSQL

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate     
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos PostgreSQL y actualizar la URL de conexión en `database.py`

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación de la API

La documentación interactiva estará disponible en:
- Swagger UI: `http://localhost:8000/docs`


### Autores
- `POST /api/v1/authors` - Crear un nuevo autor
- `GET /api/v1/authors/{id}` - Obtener un autor por ID

### Libros
- `POST /api/v1/books` - Crear un nuevo libro
- `GET /api/v1/books/{id}` - Obtener un libro por ID 