from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Country, BookCopy, Book, Author, Reader , Order , Librarian


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class BookNestedSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['genres']

class AuthorNestedSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookCopySerializer(ModelSerializer):

    book = BookNestedSerializer()

    class Meta:
        model = BookCopy
        # fields = '__all__'
        fields = ['id', 'order_number', 'book']


class AuthorSerializer(ModelSerializer):

    full_name = SerializerMethodField()

    def get_full_name(self, obj: Author) -> str:
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'country', 'full_name']


class ReaderSerializer(ModelSerializer):

    full_name = SerializerMethodField()

    def get_full_name(self, obj: Reader) -> str:
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'full_name']

class BookSerializer(ModelSerializer):
    authors = AuthorNestedSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'year_issued','authors']

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['bookcopy', 'reader', 'taken_at', 'returned_at', 'given_by']

class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = ['first_name', 'last_name', 'phone', 'employeed_date', 'unemployeed_date']


"""
1. Создать viewset и сериалайзер для модели Book. Использовать поля id, name, year_issued.
2. Добавить в BookSerializer вложенный сериалайзер AuthorSerializer для поля authors. 
В качестве полей нового сериалайзера использовать поле name.
При инициализации поля указать параметр many=True.
3. Добавить аналогичным образом сериалайзер, viewset и зарегистрировать из в router’е (urls.py) для модели Reader.
4. Добавить модель Order (см. лекционный материал на Github, models.py).
5. Добавить вьюсет и сериалайзер для Order.
6. Поле bookcopy сделать сериалайзером BookCopySerializer.
7. Поле reader сделать сериалайзером ReaderSerializer.
8. В  ReaderSerializer добавить поле full_name как SerializerMethodField, возвращая в качестве результата строку <имя+пробел+фамилия>.
"""


# AuthorNestedSerializer(many=True)