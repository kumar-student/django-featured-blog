from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from blog.forms.article_form import ArticleForm
from blog.models.articles import Article

@login_required(login_url='/login/')
def update_article_view(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    article = get_object_or_404(Article, id=id)
    if request.user == article.user or request.user.is_superuser:
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            messages.success(request,"Successfully updated, <a href='/articles/'>Articles</a>",extra_tags="text-success")
            return HttpResponseRedirect(article.get_absolute_url())
        contex = {
            "title": "Article detail",
            "article": article,
            "form": form
        }
        return render(request, "article_form.html", contex)