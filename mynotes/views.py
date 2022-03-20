from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.
@login_required
def home(request):
    notes = Note.objects.filter(author=request.user.id)
    if notes.exists():
        context = {
            'notes': reversed(notes),
            'title': 'Diginote Home'
        }
    else:
        context = {
            'title': 'Diginote Home'
        }

    return render(request, 'mynotes/home.html', context)

# the following class is not used
class NoteListView(ListView):
    model = Note
    template_name = 'mynotes/home.html'
    context_object_name = 'notes'
    ordering = ['-date_posted']

class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Make A Note'})
        return context

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context.update({'title': 'Update A Note'})
        return context

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(NoteDeleteView, self).get_context_data(**kwargs)
        context.update({'title': 'Delete'})
        return context

def search_notes(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        notes = reversed(Note.objects.filter(author=request.user.id).filter(Q(content__contains=searched) | Q(title__contains=searched)))
        context = {'searched': searched, 'notes': notes, 'title': 'Search'}

        return render(request, 'mynotes/search_notes.html', context)

    return render(request, 'mynotes/search_notes.html')
