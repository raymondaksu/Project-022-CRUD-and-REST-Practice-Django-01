from django.db import models
from django.db.models import fields
from rest_framework import serializers
from fscohort.models import Student

class StudentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='id'
    )

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]