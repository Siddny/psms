from django.db import models

# Create your models here.

# class StatusChoices(models.Model):
#     CHOICES =(
#              ('G', ('Good')),
#              ('F', ('Fair')),
#              ('B', ('Bad')))
#     name = models.CharField(max_length=200,choices=CHOICES)

#     def __str__(self):
#         return self.name

class CameraTypes(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "CameraTypes"
        verbose_name_plural = "CameraTypes"
        verbose_name = "CameraType"

    def __str__(self):
        return self.name

class CameraDetail(models.Model):
    CHOICES =(
             ('G', ('Good')),
             ('F', ('Fair')),
             ('B', ('Bad')))
    name = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, null=True, blank=False,)
    date_added = models.DateField(null=True,blank=True, auto_now=True)
    status = models.CharField(max_length=200,choices=CHOICES)
    camera_type = models.ForeignKey(CameraTypes, null=True)

    class Meta:
        db_table = "Camera"
        verbose_name_plural = "Cameras"
        verbose_name = "Camera"

    def __str__(self):
        return self.name

