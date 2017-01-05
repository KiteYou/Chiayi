from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from travel.models import Article, Comment
from travel.forms import ArticleForm


def travel(request):
    articles = Article.objects.all()
    itemsList = []
    for travel in articles:
        items = [travel]
        items.extend(list(Comment.objects.filter(article=travel)))
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'travel/travel.html', context)

def articleCreate(request):
    template = 'travel/articleCreateUpdate.html'
    if request.method == 'GET':
        print(ArticleForm())
        return render(request, template, {'articleForm':ArticleForm()})
    # POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('travel:travel')
    
def articleRead(request, articleId):
    articleToRead = get_object_or_404(Article, id=articleId)
    context = {
        'travel': articleToRead,
        'comments': Comment.objects.filter(article=articleToRead)
    }
    return render(request, 'travel/articleRead.html', context)

def articleUpdate(request, articleId):
    articleToUpdate = get_object_or_404(Article, id=articleId)
    template = 'travel/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=articleToUpdate)
        return render(request, template, {'articleForm':articleForm, 'travel':articleToUpdate})
    # POST
    articleForm = ArticleForm(request.POST, instance=articleToUpdate)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm, 'travel':articleToUpdate})
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('travel:articleRead', articleId=articleId)

def articleDelete(request, articleId):
    if request.method == 'GET':
        return travel(request)
    # POST
    articleToDelete = get_object_or_404(Article, id=articleId)
    articleToDelete.delete()
    messages.success(request, '文章已刪除')
    return redirect('travel:travel')
    
def articleSearch(request):
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'travel':articles, 'searchTerm':searchTerm}
    return render(request, 'travel/articleSearch.html', context)
    
    
    