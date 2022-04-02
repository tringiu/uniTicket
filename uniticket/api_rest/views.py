import json


from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core import serializers

from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from uni_ticket.dynamic_form import serialize_form
from uni_ticket.views.user import TicketAddNew


from . serializers import GroupSerializer, UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TicketAPIView(APIView):
    """
    Creates a new ticket.

    * 
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, structure_slug, category_slug):
        """
        Return a ticket by id
        """
        legacy_view = TicketAddNew()
        legacy_view.request = request
        legacy_response = legacy_view.get(request, structure_slug, category_slug)
        if legacy_response.status_code != 200:
            raise PermissionDenied()

        # HINT: legacy_view.title is a TicketCategory and from it we have the permissions
        # allow_anonymous
        # allow_employee
        # allow_guest
        # allow_user
        # allowed_to_user
        # allowed_users

        res = dict(
            uniticket_html_page = legacy_response.content,
            name = legacy_view.title.name,
            description = legacy_view.title.description,
            protocol_required = legacy_view.title.protocol_required,
            slug = legacy_view.title.slug,
            conditions = json.loads(serializers.serialize('json', legacy_view.title.ticketcategorycondition_set.all())),
            form = serialize_form(legacy_view.form)

        )
        return Response(res)