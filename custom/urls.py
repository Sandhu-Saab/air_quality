from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
#    path('admin/', admin.site.urls),
    path('registration/', views.showformdata, name='showformdata'),
    path('stu/', views.studentinfo),
    path('site/', views.website, name='website'),

]
