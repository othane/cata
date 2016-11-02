"""cata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from catalog import views as catalog_views
from isearch import views as isearch_views
from cata.schema import schema
from graphene.contrib.django.views import GraphQLView

# register our ReST views (part 1)
router = routers.DefaultRouter()
router.register(r'store', catalog_views.StoreViewSet, base_name='store')
router.register(r'user', catalog_views.UserViewSet, base_name='user')
router.register(r'catalog', catalog_views.CatalogItemViewSet, base_name='catalog')
router.register(r'isearch', isearch_views.ISearchViewSet, base_name='isearch')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   
    # register ReST views (part 2)
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

    # register graphql stuff
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^graphiql', include('django_graphiql.urls')),
]

if settings.DEBUG:
    # media stuff
    from django.conf.urls import patterns
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}))
