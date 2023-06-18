from django.contrib.admin import register, ModelAdmin

from movies.models import Movie, Review


@register(Movie)
class MovieAdmin(ModelAdmin):
    pass


@register(Review)
class ReviewAdmin(ModelAdmin):
    pass
