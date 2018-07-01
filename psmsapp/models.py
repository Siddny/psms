from django.db import models

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

class Employee(models.Model):
    DEPARTMENTS =(
             ('Lights', ('Lights')),
             ('Screens', ('Screens')),
             ('Sound', ('Sound')))
    name = models.CharField(max_length=200, null=False, blank=False)
    id_number = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    department = models.CharField(max_length=200, choices=DEPARTMENTS)
    designation = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "Employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name

class Equipment(models.Model):
    CHOICES =(
             ('Good', ('Good')),
             ('Fair', ('Fair')),
             ('Bad', ('Bad')))
    name = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=True, blank=False)
    p_serial_number = models.CharField(max_length=20, null=True, blank=False)
    date_added = models.DateField(null=True,blank=True, auto_now=True)
    status = models.CharField(max_length=200,choices=CHOICES)
    _type = models.CharField(max_length=20, null=True, blank=False)
    brand = models.CharField(max_length=20, null=True, blank=False)

    class Meta:
        db_table = "Equipment"
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.name

class AssignTools(models.Model):
    AVAILABILITY = (
        ('book', 'book'),
        ('assign', 'assign'),
        ('free', 'free'),
        )
    employee = models.ForeignKey(Employee, null = False)
    equipments = models.ForeignKey(Equipment, null= False)
    availability = models.CharField(max_length = 200, choices= AVAILABILITY)

    class Meta:
        db_table = "AssignTools"
        verbose_name = "AssignTools"
        verbose_name_plural = "AssignTools"