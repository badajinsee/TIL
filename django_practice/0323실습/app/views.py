from django.shortcuts import render

# Create your views here.

def number_print(request, number):
    context = {
        'number':number,
    }
    return render(request, 'app/number_print.html', context)

def calculate(request, number1, number2):
    context = {
        'number1':number1,
        'number2':number2,
        'add': number1 + number2,
        'minus': number1 - number2,
        'multiply' : number1 * number2,
        'division': number1 // number2,
    }
    return render(request, 'app/calculate.html',context)