from datetime import datetime

from .models import Language
from .models import Paradigm
from .models import Programmer

class DatabaseOperation():
    #Save object
    def save_object(self):
        language = Language(name='C++', description='C++', paradigm='Object Oriented programming')
        language.save()

    #Create object - Create and saves the object in one step
    def create_object(self):
        language = Language.objects.create(name='C++', description='C++', paradigm='Object Oriented programming')

    # Saving foreign key
    def saving_foreign_key_many_to_many(self):
        language = Language.objects.get(pk=1)
        paradigm = Paradigm.objects.get(name='Procedural')
        language.paradigm = paradigm
        language.save()

    # Updating many to many
    def updating_many_to_many(self):
        programmer = Programmer.objects.get(pk=1)
        language = Language.objects.get(name='C++')
        programmer.languages.add(language)

    # Queryset equates to SELECT and filter to WHERE or LIMIT
    # Retrieving all objects

    def retrive_all_objects(self):
        all_entries = Language.objects.all()

    #Return a new queryset matching parameters
    def filter_objects(self):
        java_language = Language.objects.filter(name='Java')

    def chaining_filters(self):
        Language.objects.filter(headline__startswith = 'What').exclude(pub_date__gte = datetime.date.today()).filter(pub_date__gte = datetime.date(2005, 1, 30))








