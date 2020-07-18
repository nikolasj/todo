## Django AdminLTE panel
### Adapted [AdminLTE](https://adminlte.io) templates for django
### Django project in Docker container with PostgreSql and Nginx


##### Used [Project](https://github.com/bandirom/django_with_docker "docker-template")  docker-template.

#### Included:
+   Python 3.8.2
+   django-allauth
+   djangorestframework
+   django-defender
+   channels
+   HTML/CSS/JS
+   Develop and production docker-template
+   PostgreSql
+   Redis
+   Nginx
+   Gunicorn
+   Daphne


### Instalation:
    git clone https://github.com/bandirom/Django-AdminLTE-templates.git

### Start dev server
    docker-compose up -d --build
    
    docker-compose logs -f

### Create superuser:
    docker-compose exec web python manage.py createsuperuser

#### Let's go to [localhost:8000](http://localhost:8000 "localhost") and check

When you first time connect to chat, you will be a chat participant

#### Stop the containers and let's try production version
    docker-compose down -v

## Production version:
    docker-compose -f prod.yml up -d --build
        
#### Check logs of your server:
    docker-compose -f prod.yml logs -f
    
    