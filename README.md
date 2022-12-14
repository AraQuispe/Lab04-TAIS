# Creamos un entorno virtual
Ejecutar `python -m venv ./venv`

# Para activar nuestro entorno virtual
Ejecutar `venv\Scripts\activate`

# Instalamos las librerías requeridas
Ejecutar `pip install -r requirements.txt`

# Creamos la base de datos
Ejecutar `python manage.py makemigrations`
Luego, ejecutar `python manage.py migrate`

# Creamos un super usuario
Ejecutar `python manage.py createsuperuser`

# Levantamos el proyecto
Ejecutar `python manage.py runserver`
El proyecto aparecerá en `http://localhost:8000/`
	