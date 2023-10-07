from django.urls import path
from main.views import NoteListView, NoteCreateView
from django.contrib.auth.decorators import login_required
from notemd.settings import LOGOUT_REDIRECT_URL


urlpatterns = [
    path('', login_required(NoteListView.as_view(), login_url=LOGOUT_REDIRECT_URL), name='notes'),
    path('create/', login_required(NoteCreateView.as_view()), name='create'),
    
]