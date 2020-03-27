from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .import forms

app_name = 'articles'

def articles_list(request):
    articles = Article.objects.all().order_by("date")
    # return HttpResponse('homepage')
    return render(request, 'articles/articles.html',{'articles' : articles})

def article_details(request,slug):
    # return HttpResponse(slug)
    artilce = Article.objects.get(slug=slug)
    return render(request,'articles/article_details.html',{'article':artilce})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/articles')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/articles_create.html', { 'form': form })

