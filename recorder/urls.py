from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fill_form/', views.fill_form, name='fill_form'),
    path('russian_speech/', views.russian_speech, name='russian_speech'),
    path('english_speech/', views.english_speech, name='english_speech'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('finish/', views.finish, name='finish'),
    path('redirect_to_recording/', views.redirect_to_recording, name='redirect_to_recording'),
]
