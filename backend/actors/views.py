from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
