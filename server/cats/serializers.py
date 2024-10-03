from rest_framework import serializers

from cats import models



class CreateCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = ('color', 'age', 'description',)

 
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, )
    class Meta:
        model = models.Cat
        fields = '__all__'

