from django.db.models import Avg
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from movies.models import Movie, Review


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title"]


class MovieFullSerializer(ModelSerializer):
    reviews = SlugRelatedField(slug_field="grade", many=True, read_only=True)
    grade_avg = SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "reviews", "grade_avg"]

    def get_grade_avg(self, obj):
        return self.instance.reviews.aggregate(grade_avg=Avg("grade"))["grade_avg"]


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {"movie": {"write_only": True}}
