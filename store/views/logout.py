from django.views import View
from django.shortcuts import render

class Logout(View):
    def get(self,request):
        request.session.clear()
        return render(request,'Login.html')
