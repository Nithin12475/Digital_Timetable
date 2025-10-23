from django.contrib import admin
from .models import Section, Faculty, Timetable, ClassSlot

admin.site.register(Section)
admin.site.register(Faculty)
admin.site.register(Timetable)
admin.site.register(ClassSlot)

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('section', 'day', 'start_time', 'end_time', 'subject', 'faculty')
    list_filter = ('section', 'day')
    search_fields = ('section', 'subject', 'faculty')