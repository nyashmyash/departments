from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(unique=True, max_length=100, null=True, blank=True)
    foto = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField(default=0, blank=True, null=True)
    age = models.PositiveIntegerField(default=0, blank=True, null=True)
    department = models.ForeignKey(to='Department', on_delete=models.PROTECT, null=False)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    director = models.ForeignKey(to='Employee', related_name='director_department', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name

    @property
    def count_employees(self):
        return len(Employee.objects.filter(department=self.id))

    @property
    def salary_employees(self):
        sum = 0
        for emp in Employee.objects.filter(department=self.id):
            sum += emp.salary
        return sum