
from django.urls import path
from .views import home,author,coments

urlpatterns = [
    path('',home),
    path('comments/',coments),
    path('authors/',author),
]