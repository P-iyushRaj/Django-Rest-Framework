from django.contrib import admin
from django.urls import path
from catalog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.stuinfo),
    path('stuinfoquery/', views.stuinfoquery),

]
