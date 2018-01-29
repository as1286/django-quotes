from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    def validate(self, form_data):
        errors = []

        # Title
        if len(form_data['title']) == 0:
            errors.append("Title is required.")
        # Author
        if len(form_data['author']) == 0:
            errors.append("Author is required.")

        return errors

    def create_book(self, form_data):
        return self.create(
            title=form_data['title'],
            author=form_data['author'],
        )

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

