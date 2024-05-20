from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.sign_in, name= 'login'),
    path("logout/", views.sign_out, name='logout'),
    path("books", views.books, name='books'),
    path("home/myBooks",views.myBooks,name='myBooks'),
    path("barrow/<str:b>", views.barrow, name='barrow'),
    path("return/<str:b>", views.returnBook, name='return'),
    path("home/manage",views.manage,name='manage')

]