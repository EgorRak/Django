from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"Country {self.name} "


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"Author {self.first_name} {self.last_name}, {self.country} "


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self):
        return f"Genre {self.name} "


class Book(models.Model):
    name = models.CharField(max_length=100)
    year_issued = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField("Author")
    pages_count = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField("Genre")
    class Meta:
        verbose_name_plural = "Books"
    def __str__(self):

        queryset = self.authors.all()
        # authors_list = [
        #     str(author) for author in queryset
        # ]
        authors_str_list= []
        for author in queryset:
            authors_str_list.append(
                str(author)
            )
        authors_str = ', '.join(authors_str_list)

        return "{} ({})".format(self.name, authors_str)

class BookCopy(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "BookCopies"

    def __str__(self):
        return f"BookCopy {self.book} {self.order_number}"

class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Readers"

    def __str__(self):
        return f"Reader {self.first_name} {self.last_name} "

class Order(models.Model):
    bookcopy = models.ForeignKey('BookCopy',on_delete=models.CASCADE)
    reader = models.ForeignKey('Reader',on_delete=models.CASCADE)
    taken_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    given_by = models.ForeignKey('Librarian',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.bookcopy} {self.reader} {self.taken_at}{self.returned_at}{self.given_by} "



class Librarian(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveSmallIntegerField()
    employeed_date = models.DateTimeField(null=True, blank=True)
    unemployeed_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Librarians"

    def __str__(self):
        return f"Librarian {self.first_name} {self.last_name} {self.phone}{self.employeed_date}{self.unemployeed_date} "







"""        Order (books actually taken):
        - id (PK)
        - bookcopy (FK -> BookCopy)
        - reader (FK -> Reader)
        - taken_at (datetime)
        - returned_at (datetime, null)
        - given_by (FK -> Librarian)
"""