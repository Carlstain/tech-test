from rest_framework.serializers import ModelSerializer

from actors.models import Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]