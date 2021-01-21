from django.conf.urls import url,include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'register/',views.register, name='register'),
    url(r'project/(\d+)',views.rate_project,name='rate-project'),
    url(r'profile/(\d+)',views.profile,name='profile'),
    url(r'my_profile',views.my_profile,name='my_profile'),
    url(r'^vote/(?P<project_id>\d+)?$', views.vote, name='vote'), 
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile', views.ProfileList.as_view(),name='api-profile'),
    url(r'^api/project', views.ProjectList.as_view(),name='api-project'),
    url(r'^api',views.api_page,name='api-page'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)