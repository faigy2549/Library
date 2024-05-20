from datetime import date

from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
from .models import Person, Book, Barrowed_book, Category
from operator import attrgetter
from datetime import timedelta
from django.utils import timezone

def register(request):
    if request.method == "POST":
        first_name_value = request.POST.get("fname")
        last_name_value = request.POST.get("lname")
        bday_value = request.POST.get("bday")
        address_value = request.POST.get("address")
        phone_value = request.POST.get("phoneNumber")
        password_value = request.POST.get("password")
        u = User.objects.create_user(
            username=first_name_value,
            password=password_value,
            first_name=first_name_value,
            last_name=last_name_value,
        )
        u.save()
        p = Person(user=u, BirthDate=bday_value, PhoneNumber=phone_value, Address=address_value)
        p.save()

        return HttpResponse(f"<h2>{first_name_value} {last_name_value} Added</h2>")

    return render(request, 'register.html')


def sign_out(request):
    logout(request)
    return redirect('index')


def home(request):
    book_list = Book.objects.all()
    user_id = request.session.get('user_id', None)
    person = Person.objects.filter(pk=user_id).first()
    bb = []

    for b in book_list:
            c = Category.objects.filter(CategoryName=b.CategoryName_id).first()
            age = date.today().year-person.BirthDate.year
            if c.AgeMin <= age:
                bb.append(b)

    admin=0
    user_logged = User.objects.filter(pk=user_id).first()
    print(f'{user_logged}')
    if user_logged.is_staff:
        admin=1
    print(f'{user_logged.is_staff}{admin}')
    data = {
        "books": bb,
        "admin":admin
    }
    return render(request, 'home.html', data)

def books(request):
    book_list = Book.objects.all()
    sorted_books = sorted(book_list, key=attrgetter('CategoryName.AgeMin'))
    data = {
        "books": sorted_books
    }
    return render(request, 'books.html', data)
def sign_in(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data["username"]
            password = loginForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return redirect('register')
    else:
        loginForm = LoginForm()

    return render(request, 'login.html', {"form": loginForm})

def barrow(request,b):
    if request.method == "POST":
        user_id = request.session.get('user_id', None)
        person=Person.objects.filter(pk=user_id).first()
        if person:
            book = Book.objects.filter(BookName=b).first()
            if book.Is_barrowed == True:
                return HttpResponse(f"<h2>the book is not available </h2>")
            category = Category.objects.filter(CategoryName=book.CategoryName_id).first()
            age =date.today().year-person.BirthDate.year


            if age >= category.AgeMin:
                borrowedBook = Barrowed_book(UserId_id=user_id, BookId_id=book.id, DateBarrowed=date.today(),ReturnDate=timezone.now() + timedelta(days=int(category.Time)))
                borrowedBook.save()
                book.Is_barrowed = True
                book.save()
                return redirect('home')

    return render(request, 'home.html')


def myBooks(request):
    user_id = request.session.get('user_id', None)
    barrowedBooks = Barrowed_book.objects.all()

    bb=[]
    for b in barrowedBooks:

            if b.UserId_id == user_id:
                bb.append(b)

    data = {
        "books": bb
    }
    return render(request, 'myBooks.html', data)
def returnBook(request,b):
    book = Book.objects.filter(BookName=b).first()
    book.Is_barrowed =False
    book.save()
    borrow = Barrowed_book.objects.get(BookId=book)
    borrow.delete()
    return redirect('myBooks')
    return render(request, 'myBooks.html')

def manage(request):
    barrowedBooks = Barrowed_book.objects.all()
    bb=[]

    for b in barrowedBooks:

            if b.ReturnDate < date.today():
                bb.append(b)

    data = {
        "books": bb
    }

    return render (request,'manage.html',data)