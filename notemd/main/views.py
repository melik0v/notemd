from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from main.models import Note
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class NoteListView(ListView):
    model = Note
    paginate_by = 20
    context_object_name = 'notes'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter()


class NoteDetailView(DetailView):
    pass

