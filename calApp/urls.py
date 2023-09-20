# calculator_app/urls.py
from django.urls import path
from calApp.views import(
  calculator
)

urlpatterns = [
    path('', calculator, name='calculator'),
]
