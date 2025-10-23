from django.shortcuts import render, redirect
from .models import Section, Timetable, ClassSlot, Faculty
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    sections = Section.objects.all()
    return render(request, 'timetable/dashboard.html', {'sections': sections})


@login_required
def create_timetable(request, section_id):
    pass
    if not request.user.is_staff:
        return redirect('dashboard')

    section = Section.objects.get(id=section_id)
    if request.method == "POST":
        date = request.POST['date']
        timetable = Timetable.objects.create(section=section, date=date)
        return redirect('add_slots', timetable_id=timetable.id)

    return render(request, 'timetable/create_timetable.html', {'section': section})

@login_required
def add_slots(request, timetable_id):
    timetable = Timetable.objects.get(id=timetable_id)

    if request.method == "POST":
        time_start = request.POST['time_start']
        time_end = request.POST['time_end']
        subject = request.POST['subject']
        faculty_id = request.POST['faculty']
        faculty = Faculty.objects.get(id=faculty_id)

        ClassSlot.objects.create(
            timetable=timetable,
            time_start=time_start,
            time_end=time_end,
            subject=subject,
            faculty=faculty
        )
        return redirect('add_slots', timetable_id=timetable_id)

    faculties = Faculty.objects.all()
    return render(request, 'timetable/add_slots.html', {'timetable': timetable, 'faculties': faculties})

@login_required
def student_timetable(request):
    user_section = request.user.profile.section  # Assuming section is part of the user profile
    timetable = Timetable.objects.filter(section=user_section).order_by('day', 'start_time')
    return render(request, 'timetable/timetables.html', {'timetable': timetable})

@login_required
def manage_timetable(request):
    timetable = Timetable.objects.all()
    return render(request, 'timetable/manage_timetable.html', {'timetable': timetable})