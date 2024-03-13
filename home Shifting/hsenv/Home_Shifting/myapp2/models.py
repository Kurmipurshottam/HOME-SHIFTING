from django.db import models
from myapp.models import *
from django.utils import timezone

# Create your models here.

class Truckpartner(models.Model):
	user = models.ForeignKey(User,on_delete =models.CASCADE,null=True)
	booking = models.ForeignKey(Booking,on_delete =models.CASCADE,null=True)
	t_name = models.CharField(max_length = 50)
	t_email = models.EmailField(unique=True , max_length = 50)
	t_contact = models.CharField(max_length = 11)
	t_password = models.CharField(max_length = 50)
	t_rcnumber = models.CharField(max_length = 10)
	t_aadharcard_details = models.CharField(max_length = 12 , unique = True)
	t_pancard_details = models.CharField(max_length = 10 , unique = True)
	t_drivinglicence_details = models.CharField(max_length = 15 , unique = True)
	t_picture = models.ImageField(default="profile/default-picture.png",upload_to="profile/")
      
	def __str__(self):
		return self.t_name + " || " + self.t_email
	
class Packages(models.Model):
   
		packages_name = models.CharField(max_length=20)
		price = models.PositiveIntegerField()
		razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
		razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
		truck = models.ForeignKey(Truckpartner, on_delete=models.CASCADE,null=True)
		start_date = models.DateTimeField(default=timezone.now)
		end_date = models.DateTimeField(null=True)

	
		def str(self):
			return self.package_name + " | |" + self.start_date
# class Pakage(models.Model):
# 	tp = models.ForeignKey(Truckpartner,on_delete = models.CASCADE)
# 	pakage_type = 
	
# class show_booking(models.model):

	



	
