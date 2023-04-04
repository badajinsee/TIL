from django.urls import path
from . import views

app_name ='articles'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:pk>',views.detail, name='detail'),
    # path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    # 데이터 삭제에 대한 url
    path('<int:pk>/delete',views.delete, name='delete'),
    # 데이터 수정 페이지 대한 URL 
    # path('<int:article_pk>/edit/', views.edit, name='edit'),
    # 데이터 수정 로직에 대한 URL 
    path('<int:article_pk>/update/', views.update, name='update'),
]