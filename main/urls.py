from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path('about/',views.about, name="about"),
    path("contact/",views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('ukcolleges/',views.ukcollege,name="ukcollege"),
    path('cancolleges/',views.cancollege,name="cancollege"),
    path('uscolleges/',views.uscollege,name="uscollege"),
    path('auscolleges/',views.auscollege,name="auscollege"),
]