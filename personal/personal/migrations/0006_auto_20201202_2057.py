# Generated by Django 3.1.3 on 2020-12-02 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_book_pages_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'verbose_name_plural': 'BookCopies'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name_plural': 'Genres'},
        ),
    ]
