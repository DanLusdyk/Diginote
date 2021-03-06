from django.urls import path
from . import views
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', views.home, name='diginotes-home'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('search_notes/', views.search_notes, name='search-notes'),
]
