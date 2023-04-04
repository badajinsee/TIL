from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'articles/new.html',context)

# def create(request):
#     # new 에서 보낸 사용자 데이터를 받아서 변수에 할당
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()

#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form':form,
#     }
#     return render(request,'articles/new.html',context)


def create(request):
    # http request method post 라면 
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # Post가 아니라면
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html',context)


def delete(request, pk):
    # 삭제 데이터 조회
    article = Article.objects.get(pk=pk)

    # 조회한 데이터 삭제
    article.delete()

    # 전체 조회 페이지 이동 
    return redirect('articles:index')


# def edit(request, article_pk):
#     # 수정할 데이터 조회
#     article = Article.objects.get(pk=article_pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article' : article,
#         'form':form,
#     }
#     return render(request, 'articles/edit.html',context)


# def update(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     # article.title = request.POST.get('title')
#     # article.content = request.POST.get('content')
#     # article.save()
#     # return redirect('articles:detail', article.pk)

#     form = ArticleForm(request.POST,instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article':article,
#         'form':form,
#     }
#     return render(request,'articles/edit.html',context)


def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
        
            form = ArticleForm(request.POST,instance=article)
            if form.is_valid():
                form.save()
            return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article' : article,
            'form':form,
        }
        return render(request, 'articles/edit.html',context)