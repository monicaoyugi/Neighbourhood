from rest_framework import serializers
from .models import Projects, Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'project_image', 'project_url')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'user', 'contact_phonenumber', 'profile_pic')