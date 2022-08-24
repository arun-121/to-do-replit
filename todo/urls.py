from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.mark_as_complete),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
]
