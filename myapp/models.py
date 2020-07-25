from django.db import models

class Database(models.Model):
    firstname = models.CharField(max_length = 60)
    lastname = models.CharField(max_length = 60)
    myid = models.IntegerField()

    def __str__(self):
        return self.firstname