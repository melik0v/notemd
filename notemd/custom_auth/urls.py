from django.urls import path, include
from custom_auth.views import index


urlpatterns = [
    path('', index, name='login'),
    path('', include('social_django.urls', namespace='social')),
]