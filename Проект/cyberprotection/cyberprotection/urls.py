from django.contrib import admin
from django.urls import path, re_path
from mainPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="main"),
    path("/", views.index, name="main"),

    re_path(r"^cyberprotection/", views.cyberprotection, name="Theory"),
    re_path(r"^mentors/", views.mentors, name="Mentors"),
    re_path(r"^event1/", views.event1, name="First Event"),
    re_path(r"^result1/", views.result1, name="First Result"),
    re_path(r"^event2/", views.event2, name="Second Event"),
    re_path(r"^result2/", views.result2, name="Second Result"),
    re_path(r"^end/", views.end, name="End"),
]
