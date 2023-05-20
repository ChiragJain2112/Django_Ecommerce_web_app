from django.contrib import admin
from django.urls import path
from .views import home
from.views import signup
from .views import login
from .views import logout
from .views import cart
from .views import checkout
from .views import orders
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('',home.Index.as_view(),name='homepage'),
    path('signup',signup.Signup.as_view(),name='signup'),
    path('Login',login.Login.as_view(),name='login'),
    path('logout',logout.Logout.as_view(),name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('checkout',checkout.Checkout.as_view(),name='checkout'),
    path('order',auth_middleware(orders.Orders.as_view()),name='order')
]
