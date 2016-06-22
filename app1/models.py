from django.db import models


class Person(models.Model):
    melicode = models.CharField(max_length=10)
    fname = models.CharField(max_length=100)

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name = 'Person'


class Mark(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __int__(self):
        return self.grade

    class Meta:
        verbose_name = 'Grade'
