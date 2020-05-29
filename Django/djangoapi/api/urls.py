from django.urls import path
from . import views

urlpatterns = [
    path('add_website', views.add_website),
    path('test', views.welcome),
    path('get_website/<int:id>', views.get_website),
    path('dashboard', views.get_dashboard),
    path('delete_website/<int:id>',views.delete_website),
    path('update_website/<int:id>',views.update_website),
    path('add_review',views.add_review),

]
