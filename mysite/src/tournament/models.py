from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name