
from rest_framework import serializers
from api.models import PatientRecord_tbl

class PatientRecordSerializer(serializers.ModelSerializer):
    ssn = serializers.SerializerMethodField()
    class Meta:
        model = PatientRecord_tbl
        fields = '__all__'
    def get_ssn(self, obj):
        return "***-**-" + obj.resourceId[-2:]
