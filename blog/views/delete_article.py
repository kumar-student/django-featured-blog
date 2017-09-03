from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from blog.models.articles import Article

@login_required(login_url='/login/')
def delete_article_view(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    try:
        Article.objects.get(id=id).delete()
    except Article.DoesNotExist:
        messages.success(request, "Unable to delete", extra_tags="text-danger")
        return HttpResponseRedirect('/articles/%s/' % id)
    messages.success(request,"Successfully deleted", extra_tags="text-success")
    return redirect("blog:articles-list")