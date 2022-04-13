from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from ..forms import CommentForm
from ..models import Article

def comment_create(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            try:
                comment.author = request.user
            except:
                pass
            comment.article = article
            comment.save()
            return redirect('wiki:article', article_title=article.title)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'article': article, 'form': form}
    return render(request, 'wiki/article.html', context)