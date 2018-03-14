from django.db import models

# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=True)
    date_added = models.DateField(blank=False, auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = "Camera"
        verbose_name_plural = "Cameras"
        verbose_name = "Camera"

    def __str__(self):
        return self.name