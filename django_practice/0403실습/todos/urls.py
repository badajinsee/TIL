from django.urls import path
from . import views

app_name ='todos'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:todo_pk>/',views.detail, name='detail'),
    path('create/',views.create, name='create'),
    path('<int:todo_pk>/delete/',views.delete, name='delete')
]

