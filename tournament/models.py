from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_3v3 = models.BooleanField(default=True)

    def __str__(self):
        return self.name