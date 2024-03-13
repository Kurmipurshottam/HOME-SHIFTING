from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random
import requests
from django.conf import settings
from django.urls import reverse
import razorpay

# Create your views here.
def delivery_signup(request):
    if request.POST:
        print(">>>>>>>>>>>page lode")
        try:
           print("=================Email Alredy exits===================")
           truckpartner = Truckpartner.objects.get(t_email = request.POST['email'])
           print(">>>>>>>>>>>>>>>>Email Alredy Exist!!!!")
           msg = "email Alredy Exist !!!!!"
           messages.error(request,msg)
           return redirect('delivery_signup')
        except:
            if request.POST['password'] == request.POST['confirm_password']:
                truckpartner = Truckpartner.objects.create(
                    t_name = request.POST['name'],
                    t_aadharcard_details = request.POST['aadhaar_card'],
                    t_pancard_details = request.POST['pan_card'],
                    t_drivinglicence_details = request.POST['driving_licence'],
                    t_rcnumber = request.POST['rc_number'],
                    t_packagetype = request.POST['package_type'],
                    t_packageprice = request.POST['package_price'],
                    t_contact = request.POST['contact'],
                    t_email = request.POST['email'],
                    t_password = request.POST['password'],
                )
                print(truckpartner.t_name)
                msg = "Your Registration Done ...."
                print("============",msg)
                messages.success(request, msg)
                return render(request,'delivery_signup.html')
                return redirect('delivery_login')
                # add ragistration than redirect login page
            else:
                pmsg="Password and Confim Password Does Not Matched !!!"
                messages.error(request, pmsg)
                return redirect('delivery_signup')
    else:
        return render(request,'delivery_signup.html')

def delivery_login(request):
    if request.POST:
        try:
            print("check password and email")
            truckpartner=Truckpartner.objects.get(t_email = request.POST['email'])
            print("hello")
            request.session['email'] = truckpartner.t_email
            request.session['name'] = truckpartner.t_name
            request.session['contact'] = truckpartner.t_contact
            request.session['password'] = truckpartner.t_password
            request.session['picture'] = truckpartner.t_picture.url
            print(">>>>>>>>>session start : ",request.session['email'])
            print(">>>>>>>>>>>> login successfully >>>>>>>>>>>>>>>>>...")
            msg = "login successfully"
            messages.success(request,msg)
            return redirect('delivery_index')  
        except: 
            msg="Your email or password is not match !!!!"
            messages.error(request,msg)
            print(msg)
            return redirect('delivery_login')
    else:
        return render(request,"delivery_login.html")
    
def delivery_logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['password']
    del request.session['contact']
    del request.session['picture']
    msg="Logout successfully"
    messages.success(request,msg)

    return redirect('delivery_login')

def delivery_index(request):
    return render(request,"delivery_index.html")

def delivery_mywallet(request):
    return render(request,"delivery_mywallet.html")

def delivery_profile(request):
    truckpartner=Truckpartner.objects.get(t_email=request.session['email'])
    return render(request,"delivery_profile.html",{'truckpartner':truckpartner})

def delivery_contact(request):
    return render(request,"delivery_contact.html")

def delivery_Withdrawal_funds(request):
    return render(request,"delivery_Withdrawal_funds.html")

def delivery_profile_update(request):
    truckpartner=Truckpartner.objects.get(t_email=request.session['email'])
    #request.session['name']=truckpartner.t_name
    if request.POST:
        truckpartner.t_name=request.POST['name']      
        truckpartner.t_contact=request.POST['contact']
        if "profile_picture" in request.FILES:      
            truckpartner.t_picture=request.FILES['profile_picture']   
        
        truckpartner.save() 

        request.session['name'] = truckpartner.t_name   
        request.session['contact'] = truckpartner.t_contact   
        request.session['picture'] = truckpartner.t_picture.url   
        msg = "Profile Updated Successfully"
        messages.success(request,msg)
        return redirect('delivery_profile')
       # return render(request,"delivery_profile.html",{'truckpartner':truckpartner})
    else:
        return render(request,"delivery_profile_update.html")


