from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class NoteListView(ListView):
    pass


class NoteDetailView(DetailView):
    pass

