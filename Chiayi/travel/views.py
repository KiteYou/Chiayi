from django.shortcuts import render


def travel(request):
    '''
    Render the travel page
    '''
    return render(request, 'travel/travel.html')