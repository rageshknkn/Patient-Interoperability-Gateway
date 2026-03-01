from symtable import Class
from django.shortcuts import render
from api.models import PatientRecord_tbl, SessionAccessLog
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import PatientRecordSerializer
from api.utils.GeneralUtils import get_client_ip

class PatientInTake(generics.ListCreateAPIView):
    serializer_class = PatientRecordSerializer
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return PatientRecord_tbl.objects.all()

    def create(self, request, *args, **kwargs):
        SessionAccessLog.objects.create(
            ip_address=get_client_ip(request),
            action="insert"

        )
        return super().create(request, *args, **kwargs)

class PatientAllView(generics.RetrieveAPIView):

    queryset = PatientRecord_tbl.objects.all()
    serializer_class = PatientRecordSerializer
    lookup_field = 'resourceId'
    def retrieve(self, request, *args, **kwargs):
        SessionAccessLog.objects.create(
            ip_address=get_client_ip(request),
            action="view"

        )
        return super().retrieve(request, *args, **kwargs)








