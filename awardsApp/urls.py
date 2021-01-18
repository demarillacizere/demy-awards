from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'register/',views.register, name='register'),
    url(r'project/(\d+)',views.rate_project,name='rate-project'),
    url(r'profile/(\d+)',views.profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)