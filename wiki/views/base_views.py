from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Article
import random

def index(request):
    return redirect('wiki:main_page')


def articles(request):
    page = request.GET.get('page', '1')
    article_list = Article.objects.order_by('-recent_edit_date')
    paginator = Paginator(article_list, 10)
    page_obj = paginator.get_page(page)
    context = {'title': '최근 변경내역', 'article_list': page_obj}
    return render(request, 'wiki/article_list.html', context)


def article(request, article_title):
    try:
        article = Article.objects.get(title=article_title)
        context = {'title': article_title, 'article': article}
        return render(request, 'wiki/article.html', context)
    except Article.DoesNotExist:
        context = {'title': article_title, 'article_title': article_title}
        return render(request, 'wiki/article_empty.html', context)



def article_search(request):
    # TODO: search 로직 수정필요
    query_article_title = request.GET.get('q')
    try:
        article = Article.objects.get(title=query_article_title)
        return redirect('wiki:article', article_title=article.title)
    except:
        context = {'title': '검색', 'query_name': query_article_title}
        return render(request, 'wiki/article_search.html', context)


def main_page(request):
    intro = Article.objects.get(title="_Alkorithms 소개")
    etc = Article.objects.get(title="_기타 문서")
    emaxx_proj = Article.objects.get(title="_E-maxx Algorithms 한국어 현지화 프로젝트")

    # motd list, must be seperated
    motd = ['$P$는 $NP$가 아닙니다', '$O(N^2)$ 보단 $O(NlogN)$, $O(NlogN)$ 보단 $O(N)$', '자매품인 Data strucktures 도 만나보세요', '앨런 튜링 vs 폰 노이만', 'Codechef Ninjas haters', 'Algorithms 와는 다릅니다', 'Built with Django']

    context = {'title': '대문', 'intro': intro, 'etc': etc, 'emaxx_proj': emaxx_proj, 'motd': random.choice(motd)}
    return render(request, 'wiki/main_page.html', context)
