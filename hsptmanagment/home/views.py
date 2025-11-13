from django.shortcuts import render
from django.http import HttpResponse
from .models import department,Doctors,Booking
from .forms import BookingForm,ContactForms
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def doctors(request):
    dict_doc ={
        'doc' : Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_doc)


def booking(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "confirmation.html")
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, "booking.html", dict_form)


def contact(request):
    if request.method == 'POST':
        form=ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contctconfirmation.html")
    form= ContactForms()
    dict_c_form={
        'form' : form
    }
    return render(request, "contact.html", dict_c_form)


def departments(request):
    dict_dept ={
        'dept': department.objects.all()
    }
    return render(request, "department.html", dict_dept)