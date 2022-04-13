from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteConfirmationForm
from ..models import Article

@login_required(login_url='common:login')
def article_create(request):
    if request.method == 'POST':
        # TODO: 중복 title 가지는 article 생성 방지 logic 구현
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.create_date = timezone.now()
            article.recent_edit_date = timezone.now()
            article.save()
            return redirect('wiki:article', article_title=article.title)
    else:
        form = ArticleCreateForm()
        try:
            form.fields['title'].initial = request.GET.get('q')
        except:
            pass
    context = {'form': form}
    return render(request, 'wiki/article_form_create.html', context)


@login_required(login_url='common:login')
def article_edit(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    if request.method == 'POST':
        form = ArticleEditForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.recent_edit_date = timezone.now()
            article.save()
            return redirect('wiki:article', article_title=article.title)
    else:
       form = ArticleEditForm(instance=article)
    context = {'form': form} 
    return render(request, 'wiki/article_form_edit.html', context)

@login_required(login_url='common:login')
def article_delete(request, article_title):
    # TODO: article delete 기능 구현, confirmation page 까지
    article = get_object_or_404(Article, title=article_title)
    if request.method == "POST":
        form = ArticleDeleteConfirmationForm(request.POST, article_title=article_title)
        if form.is_valid():
            article.delete()
            return redirect('wiki:articles')
    else:
        form = ArticleDeleteConfirmationForm(article_title=article_title)

    context = {'article': article, 'form': form}
    return render(request, 'wiki/article_form_delete.html', context)