from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('signupapi.api.urls')),
    path('boards/', include('boards.urls')),
]