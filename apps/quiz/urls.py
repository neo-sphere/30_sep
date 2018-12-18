from django.urls import path
app_name = 'quiz'
from .views import home
urlpatterns = [
    path('', home),
]
