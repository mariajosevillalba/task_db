📌 API de Gestión de Tareas – FastAPI + PostgreSQL
🧠 Descripción

Este proyecto consiste en el desarrollo de una API REST para la gestión de tareas, implementando operaciones CRUD completas y funcionalidades avanzadas como filtros, búsqueda, paginación y validaciones.

La API está construida con FastAPI, utiliza SQLAlchemy como ORM y una base de datos PostgreSQL para persistencia de datos.

🚀 Tecnologías utilizadas
Python
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Uvicorn
⚙️ Configuración del proyecto
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd task_db
2. Crear entorno virtual
python -m venv venv

Activar entorno:

venv\Scripts\activate
3. Instalar dependencias
pip install fastapi uvicorn sqlalchemy psycopg2-binary
4. Configurar la base de datos

Crear una base de datos en PostgreSQL:

CREATE DATABASE tasks_db;

Configurar la conexión en el archivo:

DATABASE_URL = "postgresql://postgres:TU_PASSWORD@localhost:5433/tasks_db"
▶️ Ejecución del proyecto
uvicorn main:app --reload

Abrir en navegador:

http://127.0.0.1:8000/docs
 (Swagger UI)
http://127.0.0.1:8000/redoc
🧩 Estructura del proyecto
task_db/
│
├── main.py          # Endpoints de la API
├── models.py        # Modelos ORM (SQLAlchemy)
├── schemas.py       # Esquemas (Pydantic)
├── database.py      # Conexión a la base de datos
📌 Funcionalidades implementadas
🟢 CRUD básico
Crear tarea
Obtener todas las tareas
Obtener tarea por ID
Actualizar tarea (PUT / PATCH)
Eliminar tarea
🚀 Funcionalidades avanzadas
🔍 Búsqueda por texto (/tasks/search?q=...)
📊 Filtro por estado (/tasks/filter/status)
⭐ Filtro por prioridad
📄 Paginación (/tasks/paginated)
🔄 Actualización parcial (PATCH)
📈 Estadísticas (/tasks/stats)
🧠 Validaciones implementadas
Longitud mínima en título
Longitud máxima en descripción
Validación de estado (pendiente, completado)
Rango de prioridad (1 a 3)
Manejo de errores HTTP
⚠️ Problemas comunes y soluciones
❌ Error 422 (Unprocessable Entity)
Verificar parámetros enviados
Validar tipos de datos
Revisar validaciones en schemas
❌ Conflicto de rutas

Si ocurre error con endpoints como /tasks/search o /tasks/paginated:

👉 Asegurarse que:

@app.get("/tasks/search")
@app.get("/tasks/paginated")

estén antes de:

@app.get("/tasks/{task_id}")
❌ Error con .dict

Usar correctamente:

task.model_dump()

(en Pydantic v2)

🎯 Objetivos del proyecto
Implementar una API REST profesional
Aplicar validaciones con Pydantic
Integrar base de datos relacional
Construir lógica de negocio real
Manejar errores correctamente
👩‍💻 Autor

Proyecto desarrollado como parte de formación en desarrollo backend con FastAPI.

🚀 Conclusión

Este proyecto demuestra cómo pasar de un CRUD básico a una API robusta, incorporando buenas prácticas, validaciones y funcionalidades avanzadas utilizadas en entornos reales.
