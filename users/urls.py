from django.urls import include, path
from . import views

urlpatterns = [
    path('test', views.sample_api),
    path('login', views.login),
    path('register2', views.signup),

]
