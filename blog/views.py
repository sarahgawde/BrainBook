from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,"article.html", {"articles" : articles})

def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'article_detail.html',{"article" : article})
   # return HttpResponse(slug)

def article_create(request):
    if request.method == "POST":
      form = forms.CreateArticle(request.POST,request.FILES)
      if form.is_valid():
         #save to db
         instance = form.save(commit=False)
         instance.author = request.user
         instance.save()
         return redirect ("articles:list")
    else:
      form = forms.CreateArticle()
      return render(request,"article_create.html",{"form" : form})


class ArticleList(APIView):

    def get(self,request):
        articless = Article.objects.all()
        serializer = ArticleSerializer(articless,many=True)
        return Response(serializer.data)

    def post(self):
        pass
