from django.shortcuts import render

# Create your views here.


def note_lists(request):
    return render(request, 'notes/note-lists.html')