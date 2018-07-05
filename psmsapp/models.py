from django.db import models
from django.conf import settings

from django.contrib.auth.models import(
    Group,
    AbstractUser,
    Permission,
    )


class User(AbstractUser):
    def __str__(self):
        return self.first_name

# class User(models.Model):
#     DEPARTMENTS =(
#              ('Lights', ('Lights')),
#              ('Screens', ('Screens')),
#              ('Sound', ('Sound')))
#     first_name = models.CharField(max_length=200, null=False, blank=False)
#     last_name = models.CharField(max_length=200, null=False, blank=False)
#     id_number = models.CharField(max_length=50, null=True, blank=True)
#     phone_number = models.CharField(max_length=50, null=True, blank=True)
#     email = models.CharField(max_length=50, null=True, blank=True)
#     department = models.CharField(max_length=200, choices=DEPARTMENTS)
#     designation = models.CharField(max_length=50, null=True, blank=True)

#     class Meta:
#         db_table = "User"
#         verbose_name = "User"
#         verbose_name_plural = "Employees"

#     def __str__(self):
#         return "%s %s"%(self.first_name,self.last_name)

class Department(Group):
    HOD =  models.ForeignKey(settings.AUTH_USER_MODEL)

class Project(Group):
    client = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    producer = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        db_table = "Project"
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    # def __str__(self):
    #     return self.name

class Equipment(models.Model):
    CHOICES =(
             ('Good', ('Good')),
             ('Fair', ('Fair')),
             ('Bad', ('Bad')))

    AVAILABILITY = (
        ('book', 'book'),
        ('assign', 'assign'),
        ('free', 'free'))

    label = models.CharField(max_length=20, null=False, blank=False)
    equipment_type = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=20, null=True, blank=True)
    serial_number = models.CharField(max_length=20, null=True, blank=False)
    status = models.CharField(max_length=200,choices=CHOICES)
    date_added = models.DateField(null=True,blank=True, auto_now=True)
    availability = models.CharField(max_length = 200, choices= AVAILABILITY, default='free')
    in_use = models.BooleanField(default=False)

    class Meta:
        db_table = "Equipment"
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.label

class DispatchToDept(models.Model):
    department = models.ForeignKey(Department, null=False)
    date_out = models.DateField(null=True, blank=True, auto_now=False)
    date_in = models.DateField(null=True, blank=True, auto_now=False)
    project = models.ForeignKey(Project, null=False)

class DispatchToolsToDept(models.Model):
    dispatch = models.ForeignKey(DispatchToDept, null=False)
    equipment = models.ForeignKey(Equipment, null=False)

class AssignTools(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    equipments = models.ForeignKey(Equipment, null= False)
    condition_ontake = models.CharField(max_length=200, null=True, blank=True)
    condition_onreturn = models.CharField(max_length=200, null=True, blank=True)
    date_taken = models.DateField(null=True,blank=True, auto_now_add=True)
    date_returned = models.DateField(null=True,blank=True, auto_now_add=True)

    class Meta:
        db_table = "AssignTools"
        verbose_name = "AssignTools"
        verbose_name_plural = "AssignTools"

    def __str__(self):
        return "%s %s"%(self.employee,self.equipments)


class CameraTypes(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "CameraTypes"
        verbose_name_plural = "CameraTypes"
        verbose_name = "CameraType"

    def __str__(self):
        return self.name

class CameraDetail(models.Model):
    CHOICES =   (
                ('Good', ('Good')),
                ('Fair', ('Fair')),
                ('Bad', ('Bad')))
    name = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=True, blank=False,)
    p_serial_number = models.CharField(max_length=20, null=True, blank=False,)
    date_added = models.DateField(null=True,blank=True, auto_now=True)
    status = models.CharField(max_length=200,choices=CHOICES)
    camera_type = models.ForeignKey(CameraTypes, null=True)

    class Meta:
        db_table = "Camera"
        verbose_name_plural = "Cameras"
        verbose_name = "Camera"

    def __str__(self):
        return self.name