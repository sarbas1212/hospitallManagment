from django.contrib import admin
from .models import department,Doctors,Booking,Contact
# Register your models here.

admin.site.register(department)

admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'Booking_date', 'booked_on')


admin.site.register(Booking, BookingAdmin)



admin.site.register(Contact)

