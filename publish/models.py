from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields
class Author(Document):
    name = fields.StringField()