from django.contrib.admin import ModelAdmin, register

from actors.models import Actor


@register(Actor)
class ActorAdmin(ModelAdmin):
    pass
