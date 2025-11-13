from django.db import models

# Create your models here.

class department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_discription=models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    dep_name=models.ForeignKey(department, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')


    def __str__(self):
        return 'Dr ' +self.doc_name +' - (' + self.doc_spec + ')'


class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name 
    



class Contact(models.Model):
    c_name=models.CharField(max_length=100)
    c_phone=models.CharField(max_length=10)
    c_email=models.EmailField()
    c_message=models.TextField()

    def __str__(self):
        return self.c_name