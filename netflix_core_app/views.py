from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_to_list(request):
    return render(request, 'add_to_list.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')