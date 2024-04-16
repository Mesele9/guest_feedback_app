from django.contrib import admin
from .models import Hotel, Feedback, Complaint, MaintenanceRequest

admin.site.register(Hotel)
#admin.site.register(Room)
#admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(Complaint)
admin.site.register(MaintenanceRequest)