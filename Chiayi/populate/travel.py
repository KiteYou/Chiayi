from populate import base
from travel.models import Article, Comment
import random

def populate():
    print('Populating Article and Comment...', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django']
    comments = ['文章真棒', '並不認同您的觀點', '借分享', '學好一個程式語言或框架並不容易']
    Article.objects.all().delete()
    Comment.objects.all().delete()
    for title in titles:
        travel = Article()
        travel.title = title
        for j in range(20):
            travel.content += title + '\n'
        travel.likes = random.randint(0, 10)
        travel.save()
        for comment in comments:
            Comment.objects.create(article=travel, content=comment)
    print('done')

if __name__ == '__main__':
    populate()