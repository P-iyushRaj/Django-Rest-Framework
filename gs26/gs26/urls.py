from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('stuapi/', views.StudentList.as_view()),
    #path('stuapi/', views.StudentCreate.as_view()),
    #path('stuapi/', views.StudentRetrive.as_view()),

    #path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
    #path('stuapi/<int:pk>/', views.StudentUpdate.as_view()),
    #path('stuapi/<int:pk>/', views.StudentDestroy.as_view()),
    path('stuapi/', views.StudentListCreate.as_view()),
    path('stuapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]


