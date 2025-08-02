from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('lists/', views.note_lists, name = 'note-lists'),
    
]