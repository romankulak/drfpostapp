# Setting up demo app

1. 
    Run with docker-compose: `docker-compose up web`

    Predefined admin user:

        Username: `admin`

        Password: `qwertyuyuiop`

    Go to `http://127.0.0.1:8000/` to see the basic posts list with search

    Or 
    Run only back-end app: `docker-compose up --no-deps web`

2.
    Test: `docker-compose run --rm --no-deps web bash -c "python manage.py test"`


### Awailable endpoints

`/` - homepage with basic post list and search

`api/v1/posts` - posts api

`api/v1/users` - users api

`api/v1/token/` - JWT obtain access and refresh tokens 

`api/v1/token/refresh/` - JWT obtain access with refresh token