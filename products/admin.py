from django.contrib import admin
from .models import Product
from .models import Offer
from .models import Student
from .models import Class
from .models import Dormitory

# Customize offer
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Customize product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Customize student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'class_name', 'dormitory_name')

    def class_name(self, obj):
        return obj.student_class.name

    def dormitory_name(self, obj):
        return obj.student_dormitory.name


class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']


class DormitoryAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Dormitory, DormitoryAdmin)