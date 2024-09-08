#! /bin/bash
set -e
worker=${WORKER:-1}
port=${DJANGO_PORT:-8080}

while ! pg_isready -h ${DATABASE_HOST:-db} -p ${DATABASE_PORT:-5432} | grep -q 'accept'; do
  echo "Cannot connect to database, retrying in 4 seconds..."
  sleep 4
done
echo "Database Ready, Starting..."

python manage.py migrate
#python manage.py loaddata scripts/fixtures/*.yaml

if [ "$PRODUCTION" == "TRUE" ]; then
  gunicorn --bind 0.0.0.0:${port} -k gevent -w ${worker} project.wsgi
else
  python manage.py runserver 0.0.0.0:${port}
fi
