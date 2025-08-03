from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ("note_name", "created_by", "note_date")
    prepopulated_fields = {"slug_link": ("note_name",)}
    

admin.site.site_header = "Keep Note Admin Panel"
admin.site.site_title = "Keep Note Admin"
admin.site.index_title = "Welcome to the Task Dashboard"


# Register your models here.
admin.site.register(Note, NoteAdmin)