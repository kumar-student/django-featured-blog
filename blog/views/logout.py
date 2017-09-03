from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import logout

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully Loged out")
    return HttpResponseRedirect('/')