"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Game, Score

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class CreateGameForm(forms.Form):
    class Meta:
        model = Game
        fields = ['name', 'date', 'number_of_teams', 'team_one_name', 'team_two_name', 'team_three_name', 'team_four_name', 'team_five_name', 'team_one_score', 'team_two_score', 'team_three_score', 'team_four_score', 'team_five_score']

    def get_game(self):
        game = Game()
        game.name = self.data['name']
        game.date = self.data['date']
        game.number_of_teams = self.data['number_of_teams']
        return game

    def get_scores(self):
        score1 = Score()
        score1.name = self.data['team_one_name']
        score1.score = self.data['team_one_score']
        score2 = Score()
        score2.name = self.data['team_two_name']
        score2.score = self.data['team_two_score']
        scorelist = []
        scorelist.append(score1)
        scorelist.append(score2)
        if int(self.data['number_of_teams']) > 2:
            score3 = Score()
            score3.name = self.data['team_three_name']
            score3.score = self.data['team_three_score']
            scorelist.append(score3)
        if int(self.data['number_of_teams']) > 3:
            score4 = Score()
            score4.name = self.data['team_four_name']
            score4.score = self.data['team_four_score']
            scorelist.append(score4)
        if int(self.data['number_of_teams']) > 4:
            score5 = Score()
            score5.name = self.data['team_five_name']
            score5.score = self.data['team_five_score']
            scorelist.append(score5)
        return scorelist