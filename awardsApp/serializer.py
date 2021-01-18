
from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('bio','email','profile_picture','user','contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('image','title','description','link','user')