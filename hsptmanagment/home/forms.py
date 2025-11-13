from django import forms
from .models import Booking,Contact


class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets ={
            'Booking_date' : DateInput(),
        }

        labels = {
            'p_name' :"Patient Name",
            'p_phone':"Phone Number",
            'p_email': "Email ID",
            'doc_name': "Doctor Name",
            'Booking_date': "Booking Date"

        }


class ContactForms(forms.ModelForm):
    class Meta:
        model= Contact
        fields = '__all__'


        labels = {
            'c_name':"Name",
            'c_phone': "Phone Number",
            'c_email': "Email ID",
            'c_message': "Message"
        }


        

