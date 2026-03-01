from django.contrib import admin
from api.models import PatientRecord_tbl, SessionAccessLog

admin.site.register(SessionAccessLog)
@admin.register(PatientRecord_tbl)
class PatientFeature(admin.ModelAdmin):
    list_display = ('resourceId', 'show_passport', 'gender', 'active')
    def show_passport(self, obj):
        return obj.get_decrypted_passport()
    show_passport.short_description = "passportNumber"