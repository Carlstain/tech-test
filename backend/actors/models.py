from django.db.models import CharField

from common.models import CreationInfoModel


class Actor(CreationInfoModel):
    first_name = CharField(verbose_name="First name", max_length=32)
    last_name = CharField(verbose_name="Last name", max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
