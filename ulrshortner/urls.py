from django.urls import include, path
from . import views

urlpatterns = [
    path('<slug:title>', views.displayShortUrl),

]
