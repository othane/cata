from rest_framework import serializers
from catalog.models import Store, CatalogItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class StoreSerializer(serializers.ModelSerializer):
    """
    This serializes the store model so the it can be viewed and edited
    """

    # add the owner as a RO field (it is populated in the view from the request
    # see perform_create)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Store 
        fields = ('owner', 'id', 'desc', 'website', 'address', 'created')


class CatalogItemSerializer(serializers.ModelSerializer):
    """
    This serializes the catalog model so the it can be viewed and edited
    """

    # add the owner as a RO field (it is populated in the view from the request
    # see perform_create)
    owner = serializers.ReadOnlyField(source='owner.username')
    #store = StoreSerializer(read_only=True, many=True)

    class Meta:
        model = CatalogItem
        fields = ('owner', 'id', 'store', 'desc', 'thumb', 'price', 'created', 'start', 'end')

    def validate(self, data):
        """
        atm just checks the start date is before the end date
        """
        if data['start'] > data['end']:
            raise serializers.ValidationError("Start date must be before end date")
        return data

