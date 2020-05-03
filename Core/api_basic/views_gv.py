# Create your views here.
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView

from .models import Article
from .serilaizers import ArticleSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# https://medium.com/the-andela-way/creating-a-djangorest-api-using-djangorestframework-part-2-1231fe949795

class GenericAPIVIEW(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin
                     ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            return self.retrieve(request)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        return self.destroy(id)


class ArticleCreateListView(CreateAPIView, ListAPIView
                            ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleCreateListView2(ListCreateAPIView
                             ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class SingleArticleView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
