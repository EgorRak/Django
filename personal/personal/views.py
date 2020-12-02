from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
def hello(request):
    return HttpResponse("OK")
def info(request):
    now = datetime.strftime(datetime.now(), '%d/%m/%Y/%H:%M:%S')
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

def test_template(request):


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

class HomePageView(TemplateView):
    template_name = 'HomePageView.html'
    def get_context_data(self,**kwargs):
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
        class book:
            def __init__(self,name,author, year,page, ex):
                self.name = name
                self.author = author
                self.year = year
                self.page = page
                self.ex = ex
        p1 = book(name=name,author=author,year=year,page=page,ex=ex)
        p2 = book(name=name2,author=author2,year=year2,page=page2,ex=ex2)
        return {"book":[p1,p2]}
        # return {
        #     'name': name,
        #     'name2': name2,
        #     'author': author,
        #     'author2': author2,
        #     'year': year,
        #     'year2': year2,
        #     'page': page,
        #     'page2': page2,
        #     'ex': ex,
        #     'ex2': ex2 }



"""class NumberView(TemplateView):
    template_name = 'numbers.html'

    def get_context_data(self, **kwargs):
        values = []

        for value in range(20):
            values.append(
                {
                    'value': value,
                    'square': value ** 2
                }
            )

        # Return context object for the template
        return {
            'values_list': values"""