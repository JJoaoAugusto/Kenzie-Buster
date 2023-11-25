from rest_framework import serializers
from .models import RatingChoices
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, allow_blank=True, default='')
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = serializers.CharField(allow_blank=True, default='')
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie
