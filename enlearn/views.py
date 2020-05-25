from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def panle_view(request):
    return render(request, "panle.html")

class addWord_view(View):

    def get(self, request):
        return render(request, "add_word.html")
    
    def post(self, request):
        pass

# Create your views here.

class register_view(View):

    def get(self, request):
        return render(request, "auth/regester.html")

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
        else:
            return HttpResponse(form.errors)

class login_view(View):
    
    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        print(request.POST["username"], request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/panle/addword")
        else:
            return render(request, "auth/login.html")
