from django.urls import include, path
from . import views

urlpatterns = [
    path('all', views.UrlList.as_view()),
    path('<slug:title>', views.displayShortUrl),

]
