from django.db import models
from myapp.models import *

# Create your models here.

class Truckpartner(models.Model):
	#user = models.ForeignKey(User,on_delete =models.CASCADE)
	t_name = models.CharField(max_length = 50)
	t_email = models.EmailField(unique=True , max_length = 50)
	t_contact = models.CharField(max_length = 11)
	t_password = models.CharField(max_length = 50)
	t_rcnumber = models.CharField(max_length = 10)
	# t_address = models.CharField(max_length = 50)
	t_aadharcard_details = models.CharField(max_length = 12 , unique = True)
	t_pancard_details = models.CharField(max_length = 10 , unique = True)
	t_drivinglicence_details = models.CharField(max_length = 15 , unique = True)
	t_picture = models.ImageField(default="profile/default-picture.png",upload_to="profile/")
      
	def __str__(self):
		return self.t_name + " || " + self.t_email

	



	
