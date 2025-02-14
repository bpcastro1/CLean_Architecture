# Bookstore API

API REST desarrollada con FastAPI siguiendo los principios de Clean Architecture para gestionar una relación 1:N entre Autores y Libros.

## Estructura del Proyecto

```
app/
├── domain/
│   ├── entities/
│   │   ├── author.py
│   │   └── book.py
│   └── repositories/
│       └── base_repository.py
├── application/
│   └── use_cases/
│       ├── author_use_cases.py
│       └── book_use_cases.py
├── infrastructure/
│   ├── database/
│   │   ├── database.py
│   │   └── models.py
│   └── repositories/
│       ├── author_repository.py
│       └── book_repository.py
└── interfaces/
    └── api/
        ├── dependencies.py
        └── routes.py
```

## Requisitos

- Python 3.8+
- PostgreSQL

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos PostgreSQL y actualizar la URL de conexión en `app/infrastructure/database/database.py`

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación de la API

La documentación interactiva estará disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Autores
- `POST /api/v1/authors` - Crear un nuevo autor
- `GET /api/v1/authors/{id}` - Obtener un autor por ID

### Libros
- `POST /api/v1/books` - Crear un nuevo libro
- `GET /api/v1/books/{id}` - Obtener un libro por ID 