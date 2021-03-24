from rest_framework import serializers
from charity_app.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['name', 'description', 'type', 'categories']

