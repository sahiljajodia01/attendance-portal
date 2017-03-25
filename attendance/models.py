from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=10 , null=True)

    def __unicode__(self):
        return self.name



class ExcelFiles(models.Model):
    name = models.CharField(max_length=30, null=True)
    sapID = models.IntegerField(null=True)
    attendancePercent = models.IntegerField(null=True)


    def __str__(self):
        return self.name


