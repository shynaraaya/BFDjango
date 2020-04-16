from django.urls import path

from todo.api.views import TaskListsView, TaskListView, TasksView, TaskView

urlpatterns = [
    path('list/', TaskListsView.as_view()),
    path('list/<int:pk>/', TaskListView.as_view()),
    path('list/<int:pk>/task/', TasksView.as_view()),
    path('list/<int:pk2>/task/<int:pk>/', TaskView.as_view()),
]