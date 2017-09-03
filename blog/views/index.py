from django.shortcuts import render

def index_view(request):
    print request.user
    print request.user.is_authenticated
    contex = {
        "title": "Home page"
    }
    # rending data to index.html template
    return render(request, "index.html", contex)