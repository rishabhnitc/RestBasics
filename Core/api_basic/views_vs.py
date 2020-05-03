# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Article
from .serilaizers import ArticleSerializer
from django.shortcuts import get_object_or_404


class ArticleApiViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query_set = Article.objects.all()
        article= get_object_or_404(query_set, pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    