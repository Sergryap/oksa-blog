from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single_blog'),
    path('courses/<slug:program_slug>/', views.program_details, name='program_details'),
    path('event/', views.event, name='event'),
    path('admissions/', views.admissions, name='admissions'),
    path('elements/', views.elements, name='elements'),
]