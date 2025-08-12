
from django.urls import path
from .views import ProjectViewSet

project_list = ProjectViewSet.as_view({'get': 'list'})
project_create = ProjectViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('', project_list, name='project-list'),
    path('clients/<int:client_pk>/projects/', project_create, name='project-create'),
]
