"""
URL configuration for notemd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from notemd.settings import LOGOUT_REDIRECT_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include(('main.urls', 'notes'), namespace='notes')),
    path('logout/', login_required(LogoutView.as_view(template_name='auth/index.html'), login_url=LOGOUT_REDIRECT_URL), name='logout'),
    path('', include('custom_auth.urls')),
]
