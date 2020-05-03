from django.urls import path
from .views import article_list_av, article_detail_av
from .views_cv import ArticleApiView, ArticleDetailApiView
from .views_func import article_list, article_detail
from .views_gv import GenericAPIVIEW, ArticleCreateListView, ArticleCreateListView2, SingleArticleView

urlpatterns = [
    path('article', article_list),
    path('detail/<int:pk>', article_detail),

    path('article_av', article_list_av),
    path('detail_av/<int:pk>', article_detail_av),

    path('article_cv', ArticleApiView.as_view()),
    path('detail_cv/<int:pk>', ArticleDetailApiView.as_view()),

    path('article_gv/', GenericAPIVIEW.as_view()),
    path('article_gv/<int:pk>/', GenericAPIVIEW.as_view()),

    #path('article_gv/', ArticleCreateListView.as_view()),
    #path('article_gv/', ArticleCreateListView2.as_view()),
    #path('article_gv/<int:pk>/', SingleArticleView.as_view()),


]
