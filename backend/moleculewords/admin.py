from django.contrib import admin
from .models import Language, Word


@admin.register(Language)
class LanguagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'words_amount', 'good_words_amount', 'medium_words_amount', 'almost_words_amount',)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    search_fields = ('word',)
    list_filter = ('language', 'known_level')
    list_display = ('word', 'language', 'translations', 'known_level')
