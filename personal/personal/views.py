from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
def hello(request):
    return HttpResponse("OK")
def info(request):
    now = datetime.now()
    return HttpResponse(now)

def get_numbers(request):
    values = []
    for value in range(28):
        values.append(
            {
                'value': value,
                'square': value ** 2
            }
        )
    print(values)
    return render(
        request=request,
        template_name='numbers.html',
        context={
            'values_list': values
        }
    )

def ivan(request):


    return render(
        request=request,
        template_name='dz.html',
        context={
        }
    )

def home_page(request):
    name = "Язык программирования Python"
    name2 = "Преступление и наказание"
    author = "Гвидо ван Россум"
    author2 = "Федор Достоевский"
    year = "2003"
    year2 = "1965"
    page = "500"
    page2 = "400"
    ex = "3"
    ex2 = "4"

    return render(
        request=request,
        template_name='dz2.html',
        context={
            'name': name,
            'name2': name2,
            'author': author,
            'author2': author2,
            'year': year,
            'year2': year2,
            'page': page,
            'page2': page2,
            'ex': ex,
            'ex2': ex2
        }
    )