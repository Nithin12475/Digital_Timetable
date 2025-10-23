from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('create_timetable/<int:section_id>/', views.create_timetable, name='create_timetable'),
    path('add_slots/<int:timetable_id>/', views.add_slots, name='add_slots'),
    path('login/', auth_views.LoginView.as_view(template_name='timetable/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('timetable/<int:section_id>/', views.student_timetable, name='student_timetable'),
    path('manage/', views.manage_timetable, name='manage_timetable'),
]
