# Connect & Chill Kumbya Beach Website

# Installation Guide

## requirements

1. Docker installation
2. Docker compose installation

```git clone git@github.com:iPelino/kumbya_beach.git```

copy and rename .env.sample  to .env and modify accordingly

## Dev Environment

Build: ```docker-compose build```

Run Django commands: ```docker-compose run --rm app sh -c "python manage.py createsuperuser"```

Run:  ```docker-compose up```

## Production Environment

Build: ```docker-compose -f docker-compose-deploy.yml build```

Run: ```docker-compose -f docker-compose-deploy up```
