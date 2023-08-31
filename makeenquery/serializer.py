from rest_framework import serializers
from .models import Makeenquery

class MakeenquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Makeenquery
        fields = '__all__'