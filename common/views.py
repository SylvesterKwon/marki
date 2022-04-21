from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from common.forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm

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


@login_required(login_url='common:login')
def settings(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('wiki:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'title': '설정', 'form': form}
    return render(request, 'common/settings.html', context)


def page_not_found(request, exception):
    return render(request, 'common/404.html', {'title': '404'})