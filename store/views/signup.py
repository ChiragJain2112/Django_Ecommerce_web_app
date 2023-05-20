from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData=request.POST
        first_name=postData.get('fname')
        last_name=postData.get('lname')
        phone=postData.get('number')
        email=postData.get('email')
        password=postData.get('password')
        print(first_name,last_name,phone,email,password)
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        customer.password=make_password(customer.password)
        customer.register()
        return redirect('homepage')