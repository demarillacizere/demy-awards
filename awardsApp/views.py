from django.shortcuts import render

def index(request):
    projects = project.objects.all().order_by('-date_posted')
    return render(request, 'index.html',{'projects':projects})

