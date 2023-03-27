from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('number-print/<int:number>/', views.number_print, name='number_print'),
    path('calculate/<int:number1>/<int:number2>/',views.calculate, name='calculate'),
]
