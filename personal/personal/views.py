from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from personal.models import Author
from personal.models import Country
from django.views import View
from personal.models import Book, BookCopy
from personal.models import Reader
from personal.models import Order
from personal.models import Librarian
import json

from rest_framework.viewsets import ModelViewSet
from personal.serializers import CountrySerializer
from personal.serializers import BookCopySerializer
from personal.serializers import AuthorSerializer
from personal.serializers import ReaderSerializer
from personal.serializers import BookSerializer
from personal.serializers import OrderSerializer
from personal.serializers import LibrarianSerializer

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

def get_authors(request):

    # queryset = Author.objects.all()
    queryset = Author.objects.exclude(
        first_name='Mikhail',
        last_name__startswith='U'

    )

    data = {
        'authors': queryset
    }
    return render(request,
                  'authors.html',
                  context=data)

def create_country(request,name: str):

    country = Country(name=name)

    country.save()

    return HttpResponse("OK")

def show_values(request, somestring: str, someintenger: int):

    data = f"String: {somestring}, quadratic: {someintenger**2}"

    return HttpResponse(data)



class CountryView(View):
    def get(self, *args, **kwargs):

        countries = Country.objects.all()

        data = []
        for c in countries:
            data.append({
                'name': c.name,
                'id': c.id
            })

        return JsonResponse(data,safe=False)

class BookView(View):
    def get(self, *args, **kwargs):

        books = Book.objects.all()

        data = []
        for c in books:
            data.append({
                'name': c.name,
                'id': c.id
            })

        return JsonResponse(data,safe=False)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class BookCopyViewSet(ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):

        readers = Reader.objects.all()
        books = Book.objects.all()
        authors = Author.objects.all()
        return {
                'readers': readers,
                'books': books,
                'authors': authors,
            }

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class LibrarianViewSet(ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer



class kiki(TemplateView):
    template_name = 'kiki.html'
    def get_context_data(self, **kwargs):

        readers = Reader.objects.all()
        books = Book.objects.all()
        authors = Author.objects.all()

        return {
                'readers': readers,
                'books': books,
                'authors': authors,
            }


"""1. Организовать домашнюю страницу библиотеки.
Требования:
адрес страницы: http://localhost:8000/home/
представление: классовое на базе TemplateView
На странице отобразить html-таблицы:
Список Читателей
Список Книг
Список Авторов
У каждой из таблиц выше добавить тег <h1> с названием таблицы.
1.1*. Добавить:
выводить только первых 5 авторов, у которых наибольшее количество книг.
выводить первые 10 книг с наименьшим количеством экземпляров, кроме тех, у которых вообще их нет.
книги, у которых менее 3 экземпляров, отмечать в таблице красным цветом шрифта.


"""