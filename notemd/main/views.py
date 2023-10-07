from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from main.models import Note
from main.forms import MDEditorForm
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


class NoteCreateView(CreateView):
    model = Note
    form_class = MDEditorForm
    success_url = reverse_lazy('notes:notes')

    def get(self, request, *args, **kwargs):
        self.object = None
        if not self.request.user.is_authenticated:
            raise Http404("Page not found")
        return super().get(request)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    


class NoteUpdateView(UpdateView):
    pass


class NoteDeleteView(DeleteView):
    pass

