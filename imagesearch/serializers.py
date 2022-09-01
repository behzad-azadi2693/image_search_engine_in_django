from rest_framework import serializers
from .models import Image



class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image')


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    
    def validate_image(self, value):
        ALLOW_FORMAT = ['png', 'jpg', 'jpeg']
        format = str(value).split('.')[1]

        if format.lower() in ALLOW_FORMAT:
            return value

        raise serializers.ValidationError('format is not accept')