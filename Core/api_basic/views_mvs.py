# Create your views here.
from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView

from .models import Article
from .serilaizers import ArticleSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# https://medium.com/the-andela-way/creating-a-djangorest-api-using-djangorestframework-part-2-1231fe949795
# https://www.django-rest-framework.org/api-guide/authentication/
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

class GenericAPIViewSet(viewsets.ModelViewSet,
                        # mixins.ListModelMixin,
                        # mixins.CreateModelMixin,
                        # mixins.UpdateModelMixin,
                        # mixins.RetrieveModelMixin,
                        # mixins.DestroyModelMixin
                        ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
