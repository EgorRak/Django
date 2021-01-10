"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personal.views import hello
from personal.views import info
from personal.views import get_numbers
from personal.views import test_template
from personal.views import home_page
from personal.views import HomePageView
from personal.views import get_authors
from personal.views import create_country
from personal.views import show_values
from personal.views import home
from personal.views import CountryView, CountryViewSet
from personal.views import BookView, BookCopyViewSet, BookViewSet
from personal.views import Author,AuthorViewSet
from personal.views import Reader,ReaderViewSet
from personal.views import OrderViewSet
from personal.views import LibrarianViewSet
from personal.views import kiki
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('countries-new', CountryViewSet)
router.register('books-copy-new', BookCopyViewSet)
router.register('authors-new', AuthorViewSet)
router.register('readers-new', ReaderViewSet)
router.register('book-new', BookViewSet)
router.register('order-new', OrderViewSet)
router.register('librarian-new', LibrarianViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('info-page/', info),
    path('numbers/',get_numbers),
    path('test-template/',test_template),
    # path('home-page/',home_page),
    path('home-page/',HomePageView.as_view()),

    path('authors/', get_authors),

    path('country/<str:name>',create_country),

    path('someendpoint/<str:somestring>/<int:someinteger>', show_values),

    path('home/', home.as_view()),

    path('countries/', CountryView.as_view()),

    path('books/', BookView.as_view()),

    path('kiki/', kiki.as_view()),


    ] +router.urls


