# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serilaizers import ArticleSerializer


# function based API view
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


# a = Article(title = "Article Title", author= 'rj', email = 'abc@xyz.com')
# a.save()
@csrf_exempt
# function based view
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)