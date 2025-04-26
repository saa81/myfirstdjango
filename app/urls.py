from django.urls import path

# from project.urls import urlpatterns
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>/', views.greet, name='greet'),
    path('boooks/', views.book_list, name='books'),
    path('index/', views.my_page, name='my_page'),
    path('pt-05/', views.pt, name='pt')
]