from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('wiki:index')
    else:
        form = UserForm()
    context = {'title': '회원가입', 'form': form}
    return render(request, 'common/signup.html', context)


def page_not_found(request, exception):
    return render(request, 'common/404.html', {'title': '404'})