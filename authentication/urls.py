from django.urls import path
from authentication import views

urlpatterns = [
    path('entrar', views.login_action, name='login'),
    path('sair', views.logout_action, name='logout'),
]
