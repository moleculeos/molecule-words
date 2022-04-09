from rest_framework import serializers
from .models import Word, Language


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['language', 'word', 'translations', 'known_level']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'words_amount', 'good_words_amount', 'medium_words_amount', 'almost_words_amount']