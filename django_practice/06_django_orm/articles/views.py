from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)


def detail(request, pk):
    article = Article.objects.get(pk=pk) # 왼쪽은 컬럼 pk 
    # print(article)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # new 에서 보낸 사용자 데이터를 받아서 변수에 할당
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 받은 데이터를 db에 저장

    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사 
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    # return render(request,'articles/create.html')

    # 이동 url 반환
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 삭제 데이터 조회
    article = Article.objects.get(pk=pk)

    # 조회한 데이터 삭제
    article.delete()

    # 전체 조회 페이지 이동 
    return redirect('articles:index')


def edit(request, article_pk):
    # 수정할 데이터 조회
    article = Article.objects.get(pk=article_pk)

    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html',context)


def update(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)