from rest_framework import serializers

from cats import models


class CreateCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cat
        fields = ("color", "age", "description", "owner", "breed",)
        read_only_fields = ("owner",)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        read_only_fields = ("owner",)
        fields = "__all__"


class CatSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True,)

    class Meta:
        model = models.Cat
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = "__all__"
