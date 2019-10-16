from django.db import models

class Test(models.Model):
    f_name = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    salary = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.f_name, self.s_name
