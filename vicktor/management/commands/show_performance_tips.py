from django.core.management.base import BaseCommand
from django.db import connection

from vicktor.models import Author, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Return all books
        # SELECT ... FROM "vicktor_book"
        qs = Book.objects.all()
        for obj in qs:
            # Bad performance: extra query per object
            # SELECT ... FROM "vicktor_author" WHERE "vicktor_author"."id" = 1
            obj.author

        # Return all books with authors
        # SELECT ... FROM "vicktor_book" INNER JOIN "vicktor_author" ON ("vicktor_book"."author_id" = "vicktor_author"."id")
        qs = Book.objects.select_related("author").all()
        for obj in qs:
            # Best performance: no extra query per object
            obj.author

        # Return all authors with all books
        # SELECT ... FROM "vicktor_author"
        # SELECT ... FROM "vicktor_book" WHERE "vicktor_book"."author_id" IN (...)
        qs = Author.objects.prefetch_related("book_set").all()
        for obj in qs:
            print(obj)
            # Best performance: no extra query per object
            obj.book_set

        print(connection.queries)
