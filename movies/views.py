from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    permission_classes = [
        IsAdminOrReadOnly
    ]
    authentication_classes = [
        JWTAuthentication
    ]

    def get(self, request: Request,) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        result = self.paginate_queryset(movies, request, self)
        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [
        JWTAuthentication
    ]
    permission_classes = [
        IsAdminOrReadOnly
    ]

    def get(self, request: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(found_movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, pk=movie_id)
        found_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
