from django.shortcuts import render
import logging

from backend_utils.logs import log_params
from backend_utils.pagination import ModelPagination
# Create your views here.


from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from publish.serializers import *
from publish.models import Author

class AuthorViewSet(ModelPagination,MongoModelViewSet):
    queryset=Author.objects.all()
    lookup_field = 'id'
    serializer_class = AuthorSerializer

    #def get_queryset(self):
    #    return Author.objects.all()

