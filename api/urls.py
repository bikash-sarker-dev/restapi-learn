
from django.urls import path

from myapp.views import index, student
urlpatterns = [
    path('index/', index),
    path('students/', student),
]