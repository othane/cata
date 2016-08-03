from rest_framework import viewsets, mixins
from rest_framework import permissions, parsers

from catalog.models import CatalogItem
from isearch.serializers import ISearchSerializer

class ISearchViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):

    serializer_class = ISearchSerializer

