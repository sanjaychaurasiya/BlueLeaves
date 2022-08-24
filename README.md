# APIs and their description.

##1. http://127.0.0.1:8000/api/v1/addSensorType/
Method Accepts - GET, POST

##2. http://127.0.0.1:8000/api/v1/addSensorType/<str:pk>/
Method Accepts - GET, PUT, PATCH, DELETE

##3. http://127.0.0.1:8000/api/v1/addSensor/
Method Accepts - GET, POST

##4. http://127.0.0.1:8000/api/v1/addSensor/<int:pk>/
Method Accepts - GET, PUT, PATCH, DELETE

##5. http://127.0.0.1:8000/api/v1/addFarmBlock/
Method Accepts - GET, POST

##6. http://127.0.0.1:8000/api/v1/addFarmBlock/<int:pk>/
Method Accepts - GET, PUT, PATCH, DELETE

##7. http://127.0.0.1:8000/api/v1/addFarmModule/
Method Accepts - GET, POST

##8. http://127.0.0.1:8000/api/v1/addFarmModule/<int:pk>/
Method Accepts - GET, PUT, PATCH, DELETE

##9. http://127.0.0.1:8000/api/v1/token/ 
Method Accepts - POST
Return Access and Refresh Token of the user detail provided.

##10. http://127.0.0.1:8000/api/v1/token/refresh/
Method Accepts - POST
Return the Access Token of the Refresh token provided.

Note- Inorder to access the APIs upto 8, you need to pass Access Token.

For Deploying the project we need to follow the instruction given in the documentation (https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
