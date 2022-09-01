from django.contrib import admin
from home import views
from django.urls import path, include

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("projects/", views.projects, name='projects'),
    path("contact/", views.contact, name='contact')
]
