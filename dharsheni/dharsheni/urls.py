from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofbulb/',views.power,name="powerofbulb"),
    path('',views.power,name="powerofbulbroot")
]