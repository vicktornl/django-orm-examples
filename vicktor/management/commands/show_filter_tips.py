from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import Count

from vicktor.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Return all millennials
        # SELECT ... FROM "vicktor_author" WHERE ("vicktor_author"."date_of_birth" >= \'1981-01-01\'::date AND "vicktor_author"."date_of_birth" <= \'1996-12-31\'::date)
        list(
            Author.objects.filter(
                date_of_birth__year__gte=1981, date_of_birth__year__lte=1996
            )
        )

        # Return all authors with more than one book
        # SELECT ..., COUNT("vicktor_book"."id") AS "num_books" FROM "vicktor_author" LEFT OUTER JOIN "vicktor_book" ON ("vicktor_author"."id" = "vicktor_book"."author_id") GROUP BY "vicktor_author"."id" HAVING COUNT("vicktor_book"."id") >= 1
        list(Author.objects.annotate(num_books=Count("book")).filter(num_books__gte=1))

        print(connection.queries)
