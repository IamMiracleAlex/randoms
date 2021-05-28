from django.db import models


class Random(models.Model):
    uuid = models.UUIDField()
    date = models.DateTimeField()