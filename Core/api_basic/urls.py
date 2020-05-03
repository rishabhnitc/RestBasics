from django.urls import path, include
from .views import article_list_av, article_detail_av
from .views_cv import ArticleApiView, ArticleDetailApiView
from .views_func import article_list, article_detail
from .views_gv import GenericAPIVIEW, ArticleCreateListView, ArticleCreateListView2, SingleArticleView
from .views_vs import ArticleApiViewSet
from .views_gvs import GenericAPIViewSet
from rest_framework.routers import DefaultRouter


# Api View Set
router = DefaultRouter()
router.register('article_vs', ArticleApiViewSet, basename='article_vs')

# Generic View Set
router_gvs = DefaultRouter()
router_gvs.register('article_gvs', GenericAPIViewSet, basename='article_gvs')

# Model View Set
router_mvs = DefaultRouter()
router_mvs.register('article_mvs', GenericAPIViewSet, basename='article_gvs')

urlpatterns = [
    path('article', article_list),
    path('detail/<int:pk>', article_detail),

    path('article_av', article_list_av),
    path('detail_av/<int:pk>', article_detail_av),

    path('article_cv', ArticleApiView.as_view()),
    path('detail_cv/<int:pk>', ArticleDetailApiView.as_view()),

    # This works for declaring generic view in a single class, note both are required for the
    # get list and get single item
    path('article_gv/', GenericAPIVIEW.as_view()),
    path('article_gv/<int:pk>/', GenericAPIVIEW.as_view()),

    # These are short hand ways of declaring the same thing with less code and more assumptions
    #path('article_gv/', ArticleCreateListView.as_view()),
    #path('article_gv/', ArticleCreateListView2.as_view()),
    #path('article_gv/<int:pk>/', SingleArticleView.as_view()),


    path('', include(router.urls)), #viewset
    path('', include(router_gvs.urls)), #generic view set
    path('', include(router_mvs.urls)), #generic view set
]
