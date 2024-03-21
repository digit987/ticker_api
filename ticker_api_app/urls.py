from django.urls import path
from .views import get_ticker_data

urlpatterns = [
    path('api/', get_ticker_data, name='ticker_api'),
]
