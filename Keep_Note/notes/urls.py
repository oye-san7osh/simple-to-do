from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('lists/', views.note_lists, name = 'note-lists'),
    path('details/<slug:slug_link>', views.note_details, name = 'note-details'),
    path('create/', views.note_create, name = 'note-create'),
    path('update/<slug:slug_link>', views.note_update, name = 'note-update'),
    path('delete/<slug:slug_link>', views.note_delete, name = 'note-delete'),
]