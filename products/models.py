from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    discount = models.FloatField()


class Class(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dormitory(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
