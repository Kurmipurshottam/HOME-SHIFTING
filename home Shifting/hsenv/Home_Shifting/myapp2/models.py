from django.db import models
from myapp.models import *

# Create your models here.

class Truckpartner(models.Model):
	user = models.ForeignKey(User,on_delete =models.CASCADE,null=True)
	booking = models.ForeignKey(Booking,on_delete =models.CASCADE,null=True)
	t_name = models.CharField(max_length = 50)
	t_email = models.EmailField(unique=True , max_length = 50)
	t_contact = models.CharField(max_length = 11)
	t_password = models.CharField(max_length = 50)
	t_rcnumber = models.CharField(max_length = 10)
	t_packagetype = models.CharField(default="silver",max_length = 50)
	t_packageprice = models.PositiveIntegerField(null=True)
	t_aadharcard_details = models.CharField(max_length = 12 , unique = True)
	t_pancard_details = models.CharField(max_length = 10 , unique = True)
	t_drivinglicence_details = models.CharField(max_length = 15 , unique = True)
	t_picture = models.ImageField(default="profile/default-picture.png",upload_to="profile/")
      
	def __str__(self):
		return self.t_name + " || " + self.t_email + " || " + self.t_packagetype
	
# class Pakage(models.Model):
# 	tp = models.ForeignKey(Truckpartner,on_delete = models.CASCADE)
# 	pakage_type = 
	
# class show_booking(models.model):

	



	
