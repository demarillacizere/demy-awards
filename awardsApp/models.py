from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models import Q


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,default='default.png')
    profile_picture =models.ImageField(upload_to= 'profiles/', blank=True, default="profiles/a.jpg")
    bio = models.CharField(max_length=500, default='No bio')
    email=models.EmailField(default='No email')
    contact = models.CharField(max_length=80)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio)
        return update_profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains=user).all()

class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='')
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)
    country = models.CharField(max_length=50)

    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = Project.objects.filter(Q(title__icontains=searchterm)|Q(description__icontains=searchterm)|Q(country__icontains=searchterm))
        return search