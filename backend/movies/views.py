from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from common.pagination_classes import DefaultMovieResultsSetPagination
from movies.serializers import MovieFullSerializer, MovieSerializer, ReviewSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieFullSerializer
    pagination_class = DefaultMovieResultsSetPagination
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["post"], url_path="review")
    def add_review(self, request, pk):
        try:
            Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound(f"Movie with id {pk} does not exist")

        request.data["movie"] = pk
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
