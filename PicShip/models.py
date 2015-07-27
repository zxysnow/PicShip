__author__ = 'v-zhuan'
from django.db import models

class User(models.Model) :
    user_name = models.CharField(max_length=30)
    gender = models.IntegerField()
    bar = models.IntegerField()
    password = models.CharField(max_length=30)

    class Meta :
        db_table = "user"

class Picture(models.Model) :
    description = models.TextField()
    user = models.ForeignKey(User)
    url = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta :
        db_table = "pictuer"

class Relation(models.Model) :
    user_1 = models.ForeignKey(User, related_name='user_1')
    user_2 = models.ForeignKey(User, related_name='user_2')
    relation = models.IntegerField()

    class Meta :
        db_table = "relation"