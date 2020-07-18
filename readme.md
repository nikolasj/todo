## Django AdminLTE panel
### Adapted [AdminLTE](https://adminlte.io) templates for django
### Django project in Docker container with PostgreSql and Nginx

##### [Project](https://github.com/bandirom/django_layout "django_layout")  without docker containers.

#### Included:
+   Python 3.8.2
+   Django-allauth
+   djangorestframework
+   django-defender
+   channels
+   Basic HTML/CSS/JS
+   Develop and production docker-template
+   PostgreSql
+   Redis
+   Nginx
+   Gunicorn
+   Daphne


### Instalation:
- ##### Create a project folder
- ##### Create a virtualenv (pipenv, virtualenv)
- ##### Copy project to a folder
- ##### Install the packages from requirement.txt:

        pip install -r Django-layout/requirements.txt
 
### Testing (from root project folder) - dev. version:


    docker-compose up -d --build
    
### In the end shout be:


    Creating <YourFolderName>_db_1 ... done
    Creating <YourFolderName>_web_1 ... done

#### Cheking of running containers:
    docker ps

##### After run the commands:
    
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    
#### Let's go to [localhost:8000](http://localhost:8000 "localhost") and check

#### Check logs of your server:
    docker-compose logs -f

#### Stopping the containers and let's go to production version
    docker-compose down -v

## Production version:
    docker-compose -f docker-compose.prod.yml up -d --build
        
#### Check logs of your server:
    docker-compose -f docker-compose.prod.yml logs -f
    
##### Run the commands:
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    docker-compose exec web python manage.py collectstatic


#### Other commands:
##### Does database exist?
##
###### For dev:
    docker-compose exec db psql --username=django_layout_db_dev --dbname=django_layout_db_dev
###### For prod:
    docker-compose exec db psql --username=django_layout_db_prod --dbname=django_layout_db_prod
#### Let's go to [localhost](http://localhost "localhost") and check

#### If you have the errors like:

+   ###### django.db.utils.OperationalError: FATAL:  database "hello_django_dev" does not exist
+   ###### Cannot create container for service db: Duplicate mount point: /var/lib/postgresql/data

#### Run the command:
        docker-compose down -v
####  And try again :)

#### If doesn't work or Nginx 500 Error, delete the volume:
        docker volume ls
        docker volume rm <YourProjectName>_postgres_data
     
#### Don't forget to make a migrations and createsuperuser
####  And try again