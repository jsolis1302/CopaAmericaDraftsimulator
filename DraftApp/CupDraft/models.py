from django.db import models

# Create your models here.

class GroupM(models.Model):
    GroupId = models.AutoField(primary_key=True)
    GroupName = models.CharField(max_length=50)


class Country(models.Model):
    CountryId = models.AutoField(primary_key=True)
    CountryFlag = models.CharField(max_length=10,default="N/A")
    CountryCode = models.CharField(max_length=100)
    CountryName= models.CharField(max_length=100)
    CountryRank = models.IntegerField( default=-1)
    CountryConf = models.CharField(max_length=100,default="N/A")
    #group = models.ForeignKey(GroupM,on_delete=models.PROTECT,blank=False, default=0)

    def __str__(self):
        return f"{self.CountryCode} {self.CountryName}"

