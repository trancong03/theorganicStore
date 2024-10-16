from django.urls import path
from neoapp import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]
