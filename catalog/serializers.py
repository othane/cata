from rest_framework import serializers
from catalog.models import CatalogItem

class CatalogItemSerializer(serializers.ModelSerializer):
    """
    This serializes the catalog model so the it can be viewed and edited
    """

    # add the owner as a RO field (it is populated in the view from the request
    # see perform_create)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CatalogItem
        fields = ('owner', 'id', 'desc', 'thumb', 'price', 'created', 'start', 'end')

    def validate(self, data):
        """
        atm just checks the start date is before the end date
        """
        if data['start'] > data['end']:
            raise serializers.ValidationError("Start date must be before end date")
        return data


