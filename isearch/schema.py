import graphene
from graphene import resolve_only_args
from graphene.core.types.custom_scalars import DateTime

class SearchNode(graphene.Interface):
    id = graphene.ID()
    img = graphene.String(description='image')
    date = DateTime('current_date')


class Query(graphene.ObjectType):
    catalog_item = relay.NodeField(CatalogNode)
    catalog = DjangoFilterConnectionField(CatalogNode)

    class Meta:
        abstract = True

