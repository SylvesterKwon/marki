from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from ..forms import CommentForm
from ..models import Article, Comment

@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
def comment_delete(request, article_title, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        if request.user == comment.author:
            comment.delete()
            return redirect('wiki:article', article_title=article_title)
        else:
            # TODO: 본인이 author 가 아닌 comment를 삭제하려고 시도할때 처리 로직
            pass
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    