# API for workout tracking

To run the server, please execute the following from the root directory:
go inside the workout (server) directory

install django and djangorestframework 
```
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt openai
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



Usage:
1. Create an account
```
curl --location 'http://127.0.0.1:8000/api/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test",
    "email": "test@gmail.com",
    "password": "test"
}'
```

2. Retrieve JWT Token
```
curl --location 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "test",
    "password": "test"
}'
```

3. Add JWT as Authorization in Request
```
curl --location 'http://127.0.0.1:8000/api/exercises/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMTQyNzA3LCJpYXQiOjE3MjMxMzkwNDUsImp0aSI6ImY5ZDQ0Y2Q1MzE5YTRhMTliMGI2OTZjMzAwYTBiMjY1IiwidXNlcl9pZCI6Mn0.ST-HqT6oLVgQfuKWb8oyrMAmE3FbC4l8zMSzvMmzpZI'
```

5. Refresh if JWT expire (Optional)
```
curl --location 'http://127.0.0.1:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data '{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzIyNTQ0NSwiaWF0IjoxNzIzMTM5MDQ1LCJqdGkiOiJkZTFlY2I1YzhhZDY0MmI2OGIwZDQ3ZWE3YWZiZTljYSIsInVzZXJfaWQiOjJ9.ow3EuIn0_mDIF5QsEeM4zLGnWRyASrh2szVP1inVZms"
}'
```


Routes:

Authentication:
- api/token: get jwt
- api/refresh: refresh jwt
- api/users: Rest API for users
- api/recommend: using personal AI to give user advice exercises
    - For this feature to work, you must create an ASSISTANT in ChatGPT and set the ASSITANT_ID in ```settings.py```

Exercises:
- api/exercises: Rest API for exercises
- api/exercises/<id>: Rest API for specific exercise

Workouts:
- api/workouts: Rest API for workouts
- api/workouts/<id>: Rest API for specific workout

Sets:
- api/sets: Rest API for sets
- api/sets/<id>: Rest API for specific set

1RM Calculator:
- api/one_rep_max/ : Rest API for 1RM calculator

One of our feature is the ability to calculate 1RM.  If you can do 100 weight for 3 reps then your exercise set is input as:
![img.png](assets/setImage.png)

Now if you calculate 1RM using our algorithm, it estimates the 1RM, i.e- the maximum weight you can lift as :
![img.png](assets/1RM.png)