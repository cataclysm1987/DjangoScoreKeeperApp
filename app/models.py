"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING)

class Game(models.Model):
    name = models.CharField(max_length=50, default='')
    date = models.DateField()
    number_of_teams = models.PositiveIntegerField(default=2, validators=[MaxValueValidator(5), MinValueValidator(2)])
    game_user_info = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)

class Score(models.Model):
    name = models.CharField(max_length=50, default = '')
    score = models.DecimalField(max_digits=20, decimal_places=2)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)