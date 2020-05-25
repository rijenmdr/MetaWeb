from django.urls import path
from . import views

urlpatterns = [
    path('add_website', views.add_website),
    path('get_website/<int:id>', views.get_website),

]
