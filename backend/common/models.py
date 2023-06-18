from django.db.models import Model, DateTimeField


class CreationInfoModel(Model):
    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True)