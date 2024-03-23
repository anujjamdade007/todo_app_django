from django.urls import path
from . import views

urlpatterns = [
    # Add Task
    path('addtask/', views.addtask , name='addtask'),
    # add mark as done feature
    path('mark_as_done/<int:pk>', views.mark_as_done , name='mark_as_done'),
    # add mark as undone feature
    path('mark_as_undone/<int:pk>',views.mark_as_undone, name='mark_as_undone'),
    # add update feature
    path('update_task/<int:pk>',views.update_task, name='update_task'),
    # delet task
    path('delete_task/<int:pk>',views.delete_task, name='delete_task'),
    
]