from django.urls import path,include
from . import views


urlpatterns = [
    path('add_website', views.add_website),
    path('test', views.welcome),
    path('get_website/<int:id>', views.get_website),
    path('dashboard', views.get_dashboard),
    path('delete_website/<int:id>',views.delete_website),
    path('delete_feedback/<int:id>',views.delete_feedback),
    path('update_website/<int:id>',views.update_website),
    path('add_review',views.add_review),
    path('get_review/<int:shopid>',views.get_review),
    path('add_message',views.add_message),
    path('search',views.search),
    path(r'password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
    # path('get_review_count',views.get_review_count),

]
