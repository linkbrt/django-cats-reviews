from rest_framework import serializers

from cats import models

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = '__all__'
