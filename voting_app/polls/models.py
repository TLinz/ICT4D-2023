from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    yes_votes = models.IntegerField(default=0)
    no_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question
