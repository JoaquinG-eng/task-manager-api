# Task Manager API

API REST para gestión de tareas con autenticación JWT, construida con FastAPI y SQLAlchemy.

## Tecnologías

- Python 3.14
- FastAPI
- SQLAlchemy + SQLite
- JWT con python-jose
- Pydantic v2

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/JoaquinG-eng/task-manager-api.git
cd task-manager-api
```

2. Crear y activar el entorno virtual
```bash
py -m venv venv
source venv/Scripts/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Crear el archivo `.env`
```env
DATABASE_URL=sqlite:///./taskmanager.db
SECRET_KEY=tuclavesecreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Correr el servidor
```bash
uvicorn app.main:app --reload
```

## Endpoints

| Método | Ruta | Descripción | Auth |
|--------|------|-------------|------|
| POST | /auth/register | Registrar usuario | No |
| POST | /auth/login | Obtener token JWT | No |
| GET | /tasks/ | Listar tareas | Sí |
| POST | /tasks/ | Crear tarea | Sí |
| PUT | /tasks/{id} | Actualizar tarea | Sí |
| DELETE | /tasks/{id} | Eliminar tarea | Sí |

## Documentación interactiva

Con el servidor corriendo, entrá a:
http://127.0.0.1:8000/docs

## Autor

Joaquin G. — [GitHub](https://github.com/JoaquinG-eng)