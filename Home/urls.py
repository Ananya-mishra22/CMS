from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("home/",views.home,name='Home'),
    path("services",views.services,name='Services'),
    #path("FAQs",views.FAQs,name='FAQs'),
    path("contact",views.contact,name='Contact'),
    path('floor-buttons/', views.floor_buttons, name='floor_buttons'),
    path('classroom-buttons/<int:floor>/', views.classroom_buttons, name='classroom_buttons'),
    path('', views.index, name='index'),
    path('form/<int:classroom>/', views.person_form, name='person_form'),
    path('submit_form/<int:classroom>/', views.submit_form, name='submit_form'),
    path('facultysignin/', views.faculty_signin, name='facultysignin'),
    path('studentsignin/', views.student_signin, name='studentsignin'),
    path('facultysignup/', views.faculty_signup, name='facultysignup'),
    path('studentsignup/', views.student_signup, name='studentsignup'),
    path('FAQs', views.classroom_form, name='classroom_form'),
    path('logout/', views.user_logout, name='logout'),
]