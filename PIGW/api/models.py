import uuid

from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet
# Model for Patientintake
class PatientRecord_tbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    resourceType = models.CharField(max_length=500, default='')
    resourceId = models.CharField(max_length=500, unique=True)
    passportNumber = models.CharField(max_length=500)
    name = models.JSONField()
    gender = models.CharField(max_length=100, default='')
    birthDate = models.DateField(null=True, blank=True)
    identifier = models.JSONField()
    telecom = models.JSONField()
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.passportNumber and not self.passportNumber.startswith("gAAAA"):
            f = Fernet(settings.PIGW_SECRET_KEY)
            self.passportNumber = f.encrypt(
                self.passportNumber.encode()
            ).decode()

        super().save(*args, **kwargs)
    def get_decrypted_passport(self):
        from cryptography.fernet import Fernet
        from django.conf import settings

        try:
            f = Fernet(settings.PIGW_SECRET_KEY)
            return f.decrypt(self.passportNumber.encode()).decode()
        except Exception as e:
            print("Decrypt error:", e)
            return self.passportNumber

    def __str__(self):
        return self.resourceType

class SessionAccessLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    action = models.CharField(max_length=100,default='Nil')
    accessed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.ip_address} - {self.ip_address} - {self.accessed_at}"


