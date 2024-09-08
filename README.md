Project
===

## Development environment
- OS: `Linux(Ubuntu 20.04)`
- IDE: `PyCharm(2023.1)`
- Language: `Python(3.9)`
- Framework: `Django(4.2)`
- Database: `PostgreSQL(13)`
- Tools: `Docker(23.0.0)`, `docker-compose(v2.15.1)`


### Run the project
1. Run `cp example.env  .env` and edit the values of the variables in the file according to.
   Example: 
   ```bash
      PRODUCTION=FALSE
      DJANGO_PORT=8080
      DJANGO_SECRET_KEY=w5fmy0c_on(5+$2ado9wtwb^gaf!mil%bt@8l$#qdbj!q
      WORKER=1
      
      DATABASE_NAME=postgres
      DATABASE_USER=postgres
      DATABASE_PASSWORD=postgres
      DATABASE_HOST=192.168.1.28
      DATABASE_PORT=5432
      
      REDIS_HOST=192.168.1.2
      REDIS_PORT=6379
      REDIS_PASSWORD=password
      
      FE_HOST=192.168.1.3
      
      CELERY_BROKER_URL=redis://:password@192.168.1.28:6379/0
      CELERY_RESULT_BACKEND=redis://:password@192.168.1.28:6379/1

   ```
2. Run the project using the docker 
   ```
   docker-compose -f docker-compose.yml up --build -d
   ```
3. You can now visit the swagger interface at:       
- `http://host:port/api/swagger`

## Project structure
```bash
.
├── api
│   ├── v1
│   │   └── urls.py
│   │   └── __init__.py
│   ├── v2
│   │   ├── urls.py
│   │   └── __init__.py
│   └── __init__.py
├── apps #A mother-folder containing all apps for our project. An app can be a django template project
│   └── example_app 
│       ├── api
│       │   ├── __init__.py
│       │   │   serializers.py
│       │   │   urls.py
│       │   │   views.py
│       │   └── 
│       ├── management
│       │   ├── commands
│       │   │   └── command.py
│       │   └── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── templates
│       ├── tests
│       ├── apps.py
│       ├── __init__.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── common # An optional folder containing common "stuff" for the entire project
│   ├── __init__.py
├── docs
│   ├── CHANGELOG.md
├── locale
│   ├── en
│   ├── ja
├── project
│   ├── settings
│   │   ├── __init__.py
│   │   │── deploy.py
│   │   └── dev.py
│   ├── asgi.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── code_scanning.sh
│   ├── start_webapi.sh
├── .coveragerc
├── .dockerignore
├── .flake8
├── .gitignore
├── .pylintrc
├── docker-compose.yml
├── Dockerfile
├── example.env
├── manage.py
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

## Usage

| period      | command                                                               | description              |
|-------------|-----------------------------------------------------------------------|--------------------------|
| development | `python manage.py makemigration`                                      | Create migrations        |
| development | `python manage.py migrate`                                            | Migrate Database         |
| development | `python manage.py runserver`                                          | Start server development |
| production  | `gunicorn --bind 0.0.0.0:${port} -k gevent -w ${worker} project.wsgi` | Start server production  | 

## Test Decorator for Metrics Collection

   Access on: http://127.0.0.1:8080/api/swagger
   ![test-create-metric-collection](https://github.com/user-attachments/assets/09cfc4a2-cd1f-47ea-94b7-b437b0a3b599)

   ![get-metric-collection-info](https://github.com/user-attachments/assets/bfa9a70e-c2dd-4612-8ab3-aeba83ce5e42)
