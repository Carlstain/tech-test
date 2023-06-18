from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, ManyToManyField, SmallIntegerField, ForeignKey, CASCADE

from actors.models import Actor
from common.models import CreationInfoModel


class Movie(CreationInfoModel):
    title = CharField(max_length=120)
    description = CharField(max_length=255, blank=True, null=True)
    actors = ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title


class Review(CreationInfoModel):
    grade = SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = ForeignKey(Movie, related_name="reviews", on_delete=CASCADE)

    def __str__(self):
        return f"{self.movie} review"
