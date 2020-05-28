from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('welcome/',views.welcome),
    path('add_website', views.add_website),
    path('get_website/<int:id>', views.get_website),
    path('update_website/<int:id>',views.update_website),
    path('delete_website/<int:id>',views.delete_website),
    path('website/', WebsiteListView.as_view()),
    # path('reset-password/verify-token/', views.CustomPasswordTokenVerificationView.as_view(),
    #      name='password_reset_verify_token'),
    # path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # url(r'^password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
