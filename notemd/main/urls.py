from django.urls import path
from main.views import NoteListView

urlpatterns = [
    path('', NoteListView.as_view(), name='notes'),
]