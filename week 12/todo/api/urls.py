from django.urls import path
from todo.api.views.views import TaskListsView, TaskListView, TasksView, TaskView
from rest_framework_extensions.routers import ExtendedSimpleRouter
from todo.api.views.viewsets import TaskListsViewSet, TasksViewSet


router = ExtendedSimpleRouter()
(
    router.register(r'list', TaskListsViewSet, basename='list')
        .register(r'task', TasksViewSet, basename='task', parents_query_lookups=['list'])
)
urlpatterns = router.urls
# urlpatterns = [
#     path('list/', TaskListsView.as_view()),
#     path('list/<int:pk>/', TaskListView.as_view()),
#     path('list/<int:pk>/task/', TasksView.as_view()),
#     path('list/<int:pk2>/task/<int:pk>/', TaskView.as_view()),
# ]