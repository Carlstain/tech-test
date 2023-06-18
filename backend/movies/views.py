from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import MovieFullSerializer, MovieSerializer, ReviewSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieFullSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSerializer
        return super().get_serializer_class()
