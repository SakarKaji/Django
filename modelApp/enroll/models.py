from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField(max_length=100)
    stupass = models.CharField(max_length=100)
    # comment = models.CharField(max_length=50, default='Not Available')  #removed
    #default value is must when adding new field else it will ask in makemigrations migrate
    #not available is shown when there is no comment value 