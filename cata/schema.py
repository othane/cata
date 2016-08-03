import graphene

import catalog.schema


class Query(catalog.schema.Query):
    pass


class Mutation(catalog.schema.Mutation):
    pass


schema = graphene.Schema(name='Image Catalog Search')
schema.query = Query
schema.mutation = Mutation

