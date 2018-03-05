from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=30)
    lastLogin =models.TimeField()
    createdBy = models.TimeField()
    modifiedBy =models.TimeField()
    createdDate = models.TimeField()
    modifiedDate = models.TimeField()


