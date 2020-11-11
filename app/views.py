from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleModelForm
from .models import Article

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blog/password_change.html', {
        'form': form
    })

from django.urls import reverse

@login_required(login_url='/login/')
def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('app:list'))
    context = {
        'form': form
    }
    return render(request, "blog/blog_create_view.html", context)


def article_update_view(request, id=id):
    obj = get_object_or_404(Article, id=id)
    form = ArticleModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "blog/blog_update_view.html", context)


def article_list_view(request):
    queryset = Article.objects.all() # list of objects
    context = {
        "object_list": queryset,
        "user":request.user,
    }
    return render(request, "blog/blog_list.html", context)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "blog/blog_detail_view.html", context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('app:article-list-view')
    context = {
        "object": obj
    }
    return render(request, "blog/blog_delete_view.html", context)



