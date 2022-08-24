from django.urls import path
from .views import AddSensorList, AddSensorDetails, FarmBlockList, FarmBlockDetails, SensorList, SensorDetails, FarmModuleList, FarmModuleDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('addSensorType/', SensorList.as_view(), name='sensor-list'),
    path('addSensorType/<str:pk>/', SensorDetails.as_view(), name='sensor-details'),
    path('addSensor/', AddSensorList.as_view(), name='add-sensor'),
    path('addSensor/<int:pk>/', AddSensorDetails.as_view(), name='add-sensor-details'),
    path('addFarmBlock/', FarmBlockList.as_view(), name='farm-block'),
    path('addFarmBlock/<int:pk>/', FarmBlockDetails.as_view(), name='farm-block-details'),
    path('addFarmModule/', FarmModuleList.as_view(), name='farm-module-list'),
    path('addFarmModule/<int:pk>/', FarmModuleList.as_view(), name='farm-module-details'),

    # JWT Authentication APIs.

    # This api is used to get the access and refresh token by passing username and password.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # This api is used to get the access token by passing refresh token.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]