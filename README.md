# proyectoFlaskPostgre
Crud vuelos

Proyecto con flask y slqalchemy y bd postgress para poder desplegarlo en heroku

## Requisitos para desplegar en escritorio
### Instalar postgre
```
sudo apt-get install postgresql postgresql-contrib
```
### Crear bd postgre
```
sudo -u postgres createuser --superuser name_of_user

sudo -u name_of_user createdb name_of_database
```

### Instalar virtualenv
```
pip3 install virtualenv
```
### Ir al directorio del repositorio y crear el entorno virtual
```
virtualenv env
source env/bin/activate
```
### Instalar las dependencias
```
pip install Flask
pip install flask_sqlalchemy
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
pip install gunicorn
```

### Migrar base de datos

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Arrancar el servidor

```
python manage.py runserver
```
### Acceder desde URL:

http://localhost:5000

## Autor 
Samuel Rivera

## DESPLEGADO EN HEROKU



