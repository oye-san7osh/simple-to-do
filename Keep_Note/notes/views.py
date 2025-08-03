from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import CreateNote

# Create your views here.


def note_lists(request):
    notelists = Note.objects.filter(created_by = request.user).order_by('-note_date')
    return render(request, 'notes/note-lists.html', {'notelists': notelists})


def note_details(request, slug_link):
    notedetail = Note.objects.get(slug_link = slug_link)
    return render(request, 'notes/note-details.html', {'notedetail': notedetail})


def note_create(request):
    if request.method == "POST":
        form = CreateNote(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit = False)
            note.created_by = request.user
            note.save()
            return redirect('notes:note-lists')
    else:
        form = CreateNote()
    return render(request, 'notes/note-create.html', {'form': form})


def note_update(request, slug_link):
    
    note = Note.objects.get(slug_link = slug_link)
    
    if request.method == "POST":
        form = CreateNote(request.POST, instance = note)
        
        if form.is_valid():
            form.save()
            return redirect('notes:note-lists')
    else:
        form = CreateNote(instance = note)
    return render(request, 'notes/note-update.html', {"form" : form})


def note_delete(request, slug_link):
    note = Note.objects.get(slug_link = slug_link)
    
    if request.method == "POST":
        note.delete()
        return redirect('notes:note-lists')
    
    return render(request, 'notes/note-delete.html', {"note" : note})