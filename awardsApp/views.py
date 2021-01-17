from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from .forms import NewProjectForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.shortcuts import render

def index(request):
    projects = Project.objects.all().order_by('-date_posted')
    return render(request, 'index.html',{'projects':projects})

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        profile=Profile.objects.create(user=user,email=user.email)
        
        return redirect('login')
    else:
        return render(request,'registration/registration_form.html')
