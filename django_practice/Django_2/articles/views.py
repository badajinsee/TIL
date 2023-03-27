from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦
# 첫번째 인자는 무조건 request
def index(request):
    context = {
        'name':'Harry',
    }
    return render(request,'index.html',context)


def dinner(request):
    foods = ['볶음밥','보쌈','서브웨이','햄버거']
    context = {
        'foods':foods,
    }
    return render(request,'dinner.html',context)


def search(request):
    return render(request, 'search.html')


def throw(request):
    return render(request,'throw.html')


def catch(request):

    data = request.GET.get('message')

    context = {
        'data' : data,
    }

    return render(request,'catch.html',context)

    