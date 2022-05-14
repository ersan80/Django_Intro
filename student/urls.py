
from django.urls import path, include
from student.views import home
from student.views import henry

urlpatterns = [
   
    path("home", home, name="home"),
    path("henry/", henry, name="henry"),
]
