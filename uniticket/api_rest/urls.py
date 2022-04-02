from django.urls import path, include, re_path

from api_rest.views import GroupViewSet, TicketAPIView, UserViewSet
from rest_framework import routers
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view


import rest_framework.urls

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
  #path('api/', include(router.urls)),
  # path('api-auth/', include(rest_framework.urls, 'rest_framework',)),
  
  path(
    'api/<slug:structure_slug>/<slug:category_slug>/ticket/new', 
    TicketAPIView.as_view(), 
    name='api-new-ticket'
  ),

]


urlpatterns += re_path(
  '^openapi$',
  get_schema_view(**{}),
  name='openapi-schema'
),

urlpatterns += re_path(
  '^openapi.json$',
  get_schema_view(
    renderer_classes = [JSONOpenAPIRenderer], **{}
  ),
  name='openapi-schema-json'
),