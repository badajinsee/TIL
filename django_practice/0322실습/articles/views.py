from django.shortcuts import render

# Create your views here.

# 1번 문제
import random

def today_dinner(request):
    foods = ['치킨','삼겹살','짜장면']
    picked = random.choice(foods)
    context = {
        'foods':foods,
        'picked':picked,
    }
    return render (request,'today_dinner.html',context)

# 2번 문제

def throw(request):
    return render(request,'throw.html')


def catch(request):

    data = request.GET.get('message')
    
    context = {
        'data': data,
    }
    
    return render(request,'catch.html', context)

# 3번 문제

def lotto_create(request):
    return render(request,'lotto_create.html')

# def lotto(request):
#     number = [int(random.choice(range(1, 46))) for _ in range(6)]

#     context = {
#         'numbers' : number,
#     }

#     return render(request,'lotto.html',context)


def lotto(request):
    num = int(request.GET.get('message'))
    lottos = []
    for i in range(num):
        lottos.append(random.sample(range(1,46), 6))
    context = {
        'lottos' : lottos,
    }
    return render(request, 'articles/lotto.html', context)
