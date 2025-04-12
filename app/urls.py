from django.urls import path

# from project.urls import urlpatterns
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>/', views.greet, name='greet')
]