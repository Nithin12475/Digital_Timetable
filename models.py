from django.contrib.auth.models import User
from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Timetable(models.Model):
    day = models.CharField(max_length=20)  # Monday, Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # HOD or Faculty

    def __str__(self):
        return f"{self.section} - {self.day} - {self.subject}"

class ClassSlot(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name="slots")
    time_start = models.TimeField()
    time_end = models.TimeField()
    subject = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} ({self.time_start} - {self.time_end})"
