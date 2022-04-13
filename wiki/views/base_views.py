from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Article

def index(request):
    # TODO: index 페이지 구현
    return redirect('wiki:main_page') # 임시로 아티클 목록으로 연결


def articles(request):
    page = request.GET.get('page', '1')
    article_list = Article.objects.order_by('-recent_edit_date')
    paginator = Paginator(article_list, 10)
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'wiki/article_list.html', context)


def article(request, article_title):
    try:
        article = Article.objects.get(title=article_title)
        context = {'article': article}
        return render(request, 'wiki/article.html', context)
    except Article.DoesNotExist:
        context = {'article_title': article_title}
        return render(request, 'wiki/article_empty.html', context)



def article_search(request):
    # TODO: search 로직 수정필요
    query_article_title = request.GET.get('q')
    try:
        article = Article.objects.get(title=query_article_title)
        return redirect('wiki:article', article_title=article.title)
    except:
        context = {'query_name': query_article_title}
        return render(request, 'wiki/article_search.html', context)


def main_page(request):
    return render(request, 'wiki/main_page.html')
