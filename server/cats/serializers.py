from rest_framework import serializers

from cats import models


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = ('color', 'age', 'description',)
       
 
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
