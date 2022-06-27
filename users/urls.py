from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    # from all devices and browsers, all associated tokens
    path('logoutall/', knox_views.LogoutAllView.as_view())
]