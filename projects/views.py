
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer
from clients.models import Client
from rest_framework.decorators import action

class ProjectViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        projects = Project.objects.filter(users=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request, client_pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectCreateSerializer(data=request.data, context={'client': client, 'request': request})
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
