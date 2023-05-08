from django.shortcuts import render
from django.views import View
# Create your views here.
from . models import *
class home(View):
    def get(self,request):
        return render(self.request,"home.html")
    

class corporate(View):
    def get(self,request):
        return render(self.request,"corporate.html")
    
class contact(View):
    def get(self,request):
        return render(self.request,"contact.html")
    
    def post(self,request):
        name=request.POST.get("h_name")
        email=request.POST.get("h_email")
        number=request.POST.get("h_number")
        desc=request.POST.get("mss")
        print(name)
        print(email)
        print(number)
        print(desc)
        Contact(name=name,email=email,phone=number,desc=desc).save()
        return render(self.request,"contact.html")

class about(View):
    def get(self,request):
        return render(self.request,"about.html")
    

class gallery(View):
    def get(self,request):
        return render(self.request,"gallery.html")
    

class wedding(View):
    def get(self,request):
        return render(self.request,"wedding.html")
    
class party(View):
    def get(self,request):
        return render(self.request,"party.html")


class artist(View):
    def get(self,request):
        return render(self.request,"artist.html")
    
    
class fest(View):
    def get(self,request):
        return render(self.request,"fest.html")
    
    
class propety(View):
    def get(self,request):
        return render(self.request,"propartyexpor.html")
    
    
class cateringervices(View):
    def get(self,request):
        return render(self.request,"creatingservices.html")
    
    
    
