from django.urls import path

from .views import home,contact, about

urlpatterns = [
    path('', home, name="home"),    
    path('aaa/contact/', contact, name="contact"),
    path('bbb/about/', about, name="about"),    
    
]
