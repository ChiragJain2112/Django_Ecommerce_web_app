from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.

class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=None
        request.session.get('cart')
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
           products=Product.get_all_product_by_categoryid(categoryID)
           data={}
           data['products']=products
           data['categories']=categories
           return render(request,'index.html',data)
        else:
          products=Product.get_all_product()
          data={}
          data['products']=products
          data['categories']=categories
          return render(request,'index.html',data)

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        print(product)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=1+quantity
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        return redirect('homepage')


