from django.shortcuts import render

def login_view(request):
    contex = {
        "title": "Login"
    }
    return render(request, "login.html", contex)