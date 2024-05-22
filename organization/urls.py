from django.urls import path
from .views import register, login_organization, logout_organization
url_patterns = [
    path('sign-up/', register, name='register'),
    path('sign-in/', login_organization, name='login'),
    path('logout/', logout_organization, name='logout')
]