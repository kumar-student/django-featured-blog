from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render

from blog.forms.article_form import ArticleForm

@login_required(login_url='/login/')
def create_article_view(request):
    if not request.user.is_authenticated():
        raise Http404
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        article.save()
        messages.success(request,"Successfully created <a href='/articles/'>Articles</a>",extra_tags="text-success")
        return HttpResponseRedirect(article.get_absolute_url())

    contex = {
        "title": "Create an article",
        "form": form
    }
    return render(request, "article_form.html", contex)