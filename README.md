# API for workout tracking

To run the server, please execute the following from the root directory:
go inside the workout (server) directory

install django and djangorestframework 
```

pip install django djangorestframework  psycopg2-binary rest_framework_simplejwt  
```

make migrations and run
```
python manage.py makemigrations
python manage.py migrate
```

run the server
```
python manage.py runserver
```

Note: You might have to install some other package as needed.

You will have to create database for postgres with name "workoutdb" 
