from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/spisok/', views.spisok, name='spisok'),
    path('spisok/add/', views.spisok_add, name='spisok_add'),
    path('', views.false_index, name='false_index'),
    path('tasks/<int:spisok_id>/', views.tasks, name='tasks'),
    path('delete_spisok/<int:del_id>/', views.delete_spisok, name='delete_spisok'),
    path('add_tasks/<int:spisok_id>/', views.add_tasks, name='add_tasks'),



]