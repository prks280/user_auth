from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Neta(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    ward_no = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.party, self.area)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neta = models.ForeignKey(Neta, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return '{}{}'.format(self.user, self.neta)

    class Meta:
        unique_together = (('neta','user'))
