from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self,request):
        return render(request,'Login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer= Customer.get_customer(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id

                return redirect('homepage')
            else:
                error_message="Email or Password Invalid..."
        else:
            error_message="Email or Password Invalid..."
        print(customer)
        print(email,password)
        return render(request,'Login.html',{'error':error_message})





