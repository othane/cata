import graphene
from graphene.core.types.custom_scalars import DateTime
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode
from graphql_relay.node.node import from_global_id

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from catalog.models import Store, CatalogItem

class UserNode(DjangoNode):
    rid = graphene.IntField()

    def resolve_rid(self, args, info):
        return self.id

    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'username': ['exact'],
        }


class StoreNode(DjangoNode):
    rid = graphene.IntField()

    def resolve_rid(self, args, info):
        return self.id

    class Meta:
        model = Store 
        filter_fields = {
            'id': ['exact'],
            'desc': ['exact', 'icontains', 'istartswith'],
        }


class CatalogNode(DjangoNode):
    rid = graphene.IntField()

    def resolve_rid(self, args, info):
        return self.id

    class Meta:
        model = CatalogItem
        filter_fields = {
            'id': ['exact'],
            'store': ['exact'],
            'desc': ['exact', 'icontains', 'istartswith'],
            'start': ['exact', 'lt', 'gt'],
            'end': ['exact', 'lt', 'gt'],
        }
        filter_order_by = ['start', 'end', 'desc']


class NewCatalogItem(graphene.Mutation):
    catalog_item = graphene.Field(CatalogNode)

    class Input:
        id = graphene.String()
        store = graphene.Int()
        desc = graphene.String()
        thumb = graphene.String()
        price = graphene.Float()
        created = DateTime()
        start = DateTime()
        end = DateTime()

    @classmethod
    def mutate(cls, input, args, info):
        # be a hack user for now until I work out authentication
        user = User.objects.get_by_natural_key('graphene')
        id = args.get('id')
        if id is not None:
            # update an existing item
            rid = from_global_id(id)[1]
            catalog_item = CatalogItem.objects.get(pk=rid)
            for a,v in args.items():
                if a == 'id':
                    continue
                if hasattr(catalog_item, a):
                    setattr(catalog_item, a, v)
            catalog_item.save()
            catalog_item.refresh_from_db()
        else:
            # make a new item
            catalog_item = CatalogItem(owner=user, **args)
            catalog_item.save()
        return NewCatalogItem(catalog_item=CatalogNode(catalog_item))


class Query(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserNode)
    stores = DjangoFilterConnectionField(StoreNode)
    catalog = DjangoFilterConnectionField(CatalogNode)

    class Meta:
        abstract = True


class Mutation(graphene.ObjectType):
    catalog_item = graphene.Field(NewCatalogItem)
    
    class Meta:
        abstract = True

