from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from catalog.models import CatalogItem
from catalog.serializers import CatalogItemSerializer


class CatalogItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogItem.objects.all()
    serializer_class = CatalogItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def update(self, request, pk=None, **kwargs):
        print "updating {}".format(pk)
        return super(CatalogItemViewSet, self).update(request, pk, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


