from django.http import Http404
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.models.articles import Article
from blog.models.comments import Comment
from blog.forms.comment_form import CommentForm

@login_required(login_url='/login/')
def article_detail_view(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    article = get_object_or_404(Article,id=id)
    comments = Comment.objects.filter(article=article)

    if request.method == "POST":
        comment = request.POST.get('comment',None)
        if comment:
            Comment.objects.create(comment=comment,user=request.user,article=article)
            messages.success(request,"Successfully commented")
            return HttpResponseRedirect('/articles/%s/' % id)
    contex = {
        "title": "Article detail",
        "article": article,
        "comments": comments
    }
    return render(request,"article_detail.html",contex)