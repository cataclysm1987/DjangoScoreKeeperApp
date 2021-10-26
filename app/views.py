"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Score, Game, UserInfo

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        try:
            games = Game.objects.filter(game_user_info_id=request.user.id).order_by('-date')[:10]
            if len(games) > 0:
                return render(request, 'app/index.html', {'games': games} )
            return render(request, 'app/index.html', {'games' : None })
        except:
            return render(request, 'app/index.html', {'games' : None })
    return render(request, 'app/index.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
