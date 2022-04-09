from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import WordSerializer, LanguageSerializer
from .models import Language, Word


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Language.objects.all()


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Word.objects.filter(language__name=self.request.GET.get('language', default=''))

