from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'description', 'paradigm')


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'name')

class ProgrammerSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)
    class Meta:
        model = Programmer
        fields = ('id', 'name', 'languages')