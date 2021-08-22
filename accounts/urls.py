from django.urls import path

from . import views
from django.contrib.auth import login, views as auth_views


urlpatterns = [
    path('accounts/register/', views.register_request, name="register"),
    path('accounts/login/', views.login_request, name="login"),
    path('accounts/logout/', views.logout_request, name="logout"),
    path('accounts/logout/', views.logout_request, name="logout"),
    # path('accounts/password_change/', views.logout_request, name='password_change'),
    # path('accounts/password_change/done/', views.logout_request, name='password_change_done'),
    path('accounts/password_reset/', views.password_reset_request, name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]