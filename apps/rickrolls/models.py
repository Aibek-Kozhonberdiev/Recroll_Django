from django.core.exceptions import ValidationError
from django.db import models


class RickrollUrl(models.Model):
    url = models.TextField(max_length=5000)
    number_of_transitions = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk and RickrollUrl.objects.exists():
            raise ValidationError('Можно создать только один экземпляр RickrollUrl')
        super().save(*args, **kwargs)
