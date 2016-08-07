from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from rest_framework import permissions

from catalog.models import Store, CatalogItem
from django.contrib.auth.models import User
from catalog.serializers import UserSerializer, StoreSerializer, CatalogItemSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (permissions.IsAuthenticated,)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def update(self, request, pk=None, **kwargs):
        print "updating {}".format(pk)
        return super(StoreViewSet, self).update(request, pk, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CatalogItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogItem.objects.all()
    serializer_class = CatalogItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def update(self, request, pk=None, **kwargs):
        print "updating {}".format(pk)
        return super(CatalogItemViewSet, self).update(request, pk, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

