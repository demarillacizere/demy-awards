from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from .forms import NewProjectForm,ProfileUpdateForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
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
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            profile=Profile.objects.create(user=user,email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'registration/registration_form.html')

@login_required(login_url='/accounts/login/') 
def rate_project(request,project_id):
    project=Project.objects.get(id=project_id)
    print(project.title)
    return render(request,"project.html",{"project":project})
@login_required(login_url='/accounts/login/') 
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(user=profile.user).all()
    print(profile.user)
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'projects':projects,
        'profile':profile,
    }
    return render(request,"my_profile.html",context=context)



@login_required(login_url='/accounts/login/') 
def profile(request,profile_id):
    profile = Profile.objects.get(id=profile_id)
    projects = Project.objects.filter(user=profile.user).all()
    print(profile.user)
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'projects':projects,
        'profile':profile,
    }
    return render(request,"profile.html",context=context)

@login_required(login_url='/accounts/login/')     
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')
        
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form":form, "current_user":current_user})
    

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search(search_term)
        print(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')   
def api_page(request):
    return render(request,'api_page.html')


class ProfileList(APIView):
    def get(self, request, fromat=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, fromat=None):
        all_projects =Project.objects.all()
        serializers =ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
