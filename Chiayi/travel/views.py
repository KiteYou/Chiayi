from django.shortcuts import render
from travel.models import Article, Comment


def travel(request):
    '''
    Render the travel page
    '''
    articles = Article.objects.all()
    itemsList = []
    for travel in articles:
        items = [travel]
        items.extend(list(Comment.objects.filter(article=travel)))
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'travel/travel.html', context)