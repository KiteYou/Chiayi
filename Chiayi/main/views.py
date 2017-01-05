from django.shortcuts import render
import datetime


def main(request):
    '''
    Show 'Hello world' in the main page
    '''
    context = {'like':'歡迎拜訪此網站,這裡提供不錯的 ~ 嘉義の景點 ~', 'now':datetime.datetime.now()}
   
    return render(request, 'main/main.html', context)

def news(request):
    '''
    Render the about page
    '''
    return render(request, 'main/news.html')
