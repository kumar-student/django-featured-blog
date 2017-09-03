from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from blog.models.articles import Article

def articles_list_view(request):
    qry = Article.objects.filter(publish_date__lte=timezone.now())
    search = request.GET.get("search")
    if search:
        qry = Article.objects.filter(publish_date__lte=timezone.now()).filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(publish_date__icontains=search)
        )
    paginator = Paginator(qry, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    contex = {
        "title": "Articles",
        "articles": articles
    }
    return render(request, "articles.html", contex)