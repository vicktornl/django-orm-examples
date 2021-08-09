from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("vicktor.Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
