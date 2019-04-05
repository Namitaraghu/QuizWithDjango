from django.db import models


class Quiz(models.Model):
    question = models.CharField(max_length=283)
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
