"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Score, Game, UserInfo
from .forms import CreateGameForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator


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

@login_required
def creategame(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            game = form.get_game()
            scores = form.get_scores()
            try:
                game.game_user_info = UserInfo.objects.get(user_id = request.user.id)
            except:
                userinfo = UserInfo()
                userinfo.user = request.user
                userinfo.save()
                game.game_user_info = userinfo
            game.save()
            for score in scores:
                score.game = game
                score.save()
            games = Game.objects.filter(game_user_info_id = request.user.id)
            return redirect('/', { 'games' : games })
    form = CreateGameForm()
    return render(request, 'app/creategame.html', { 'form' : form })

@login_required
def viewgame(request, id):
    game = Game.objects.get(id = id)
    if game.game_user_info_id != request.user.id:
        games = Game.objects.filter(game_user_info_id=request.user.id).order_by('-date')[:10]
        if len(games) > 0:
            return render(request, 'app/index.html', {'games': games} )
        return render(request, 'app/index.html', {'games' : None })
    if game is not None:
        scores = Score.objects.filter(game_id = game.id)
        return render(request, 'app/viewgame.html', { 'game': game, 'scores': scores })

@login_required
def viewgames(request):
    game_list = Game.objects.all()
    paginator = Paginator(game_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/viewgames.html', {'page_obj': page_obj})

class GameListView(ListView):
    paginate_by = 2
    model = Game