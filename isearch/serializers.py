from rest_framework import serializers

class ISearchSerializer(serializers.Serializer):
    """
    represents the model-less interaction when
    the user searches for an image
    """
    img = serializers.ImageField('image')
    date = serializers.DateField('current_date', write_only=True)

    class Meta:
        fields = ('img', 'date')

    def create(self, validated_data):
        print "creating {}".format(validated_data)

