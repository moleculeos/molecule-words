import re
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Language(models.Model):
    name = models.CharField(max_length=50)

    @property
    def words_amount(self):
        return len(self.words)

    @property
    def good_words_amount(self):
        return self.words.filter(known_level=2)
    
    @property
    def medium_words_amount(self):
        return self.words.filter(known_level=1)

    @property
    def almost_words_amount(self):
        return self.words.filter(known_level=0)

    def __str__(self):
        return self.name


class Word(models.Model):
    language = models.ForeignKey(Language, related_name='words', on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    translations = models.TextField()
    known_level = models.IntegerField(validators=[MaxValueValidator(2), MinValueValidator(0)])

    def __str__(self):
        return self.word