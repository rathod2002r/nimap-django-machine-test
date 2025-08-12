from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_name', 'users']

    def create(self, validated_data):
        users = validated_data.pop('users')
        client = self.context['client']
        project = Project.objects.create(client=client, created_by=self.context['request'].user, **validated_data)
        project.users.set(users)
        return project

