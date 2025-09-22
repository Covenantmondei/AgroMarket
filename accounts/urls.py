from django.urls import path
from .views import *

urlpatterns = [
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('update-farmer/', UpdateFarmerView.as_view(), name='update-farmer'),
]