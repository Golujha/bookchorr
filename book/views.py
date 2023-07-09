from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import PostForm




def homepage(r):
    data = {}
    data['generous'] = Generous.objects.all()
    data['create'] = Books.objects.all()
    
    return render(r,"home.html",data)

@login_required()
def insert(r):
    if r.method == "POST":
        p = PostForm(r.POST,r.FILES)
        if p.is_valid():
            p.save()
        return redirect(homepage)

    return render(r,"insert.html",{"form":PostForm})


def viewPost(r,cat_id):
    data = {}
    data['generous'] = Generous.objects.all()
    data['create'] = Books.objects.filter(generous=cat_id)
    return render(r,"home.html",data)

def search(r):
    search = r.GET.get("search")
    data = {
        "generous":Generous.objects.all(), 
        "create":Books.objects.filter(title__icontains=search),
        }
    return render(r, "home.html",data)
  

def singlePost(r,post_id):
    data = {}
    data['generous'] = Generous.objects.all()
    data['show'] = Books.objects.get(pk=post_id)
   
    data['create'] = Books.objects.exclude(pk=post_id)
    return render(r,"view.html",data)

def deleteBooks(r, id):
    books = Books.objects.get(pk=id)
    books.delete()
    return redirect(homepage)

def editBooks(r, id):
    books = Books.objects.get(pk=id)
    form = PostForm(r.POST or None,r.FILES or None, instance=books)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)

    return render(r, "editBooks.html", {"form":form})

def viewBooks(r,id):
    data = {}
    data['generous'] = Generous.objects.all()
    data['create'] = Books.objects.filter(generous=id)
    return render(r,"viewBooks.html",data)




def signUp(r):
    form = UserCreationForm(r.POST or None)
    data = {
        "form":form
    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(signIn)
    return render(r,"accounts/register.html",data) 

def signIn(r):
    form = AuthenticationForm(r.POST or None)
    data = {
        "form":form
    }

    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(r,user)
            return redirect(homepage)
    return render(r,"accounts/login.html",data)


def signOut(r):
    logout(r)
    return redirect(homepage)