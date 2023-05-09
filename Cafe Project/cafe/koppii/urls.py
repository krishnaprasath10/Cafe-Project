from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home-page"),
    
    path('home.html/',views.home,name="home-page"),
    path('about.html/',views.about,name="about-page"),
    path('menu.html/',views.menu,name="menu-page"),
    path('service.html/',views.service,name="service-page"),
    path('reservation.html/',views.reservation,name="reservation-page"),
    path('contact.html/',views.contact,name="contact-page"),
    path('testimonial.html/',views.testimonial,name="testimonial-page"),
    path('signin.html/',views.signin,name="signin-page"),
    path('login.html/',views.login,name="login-page"),
    path('cart.html/',views.cart,name="cart-page"),
    
    path('reservation/',views.in_reservation,name="reservation"),
    path('contact/',views.in_contact,name="contact"),
    path('sign/',views.in_signin,name="sign"),
    path('login/',views.in_login,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('cart/',views.cart_page,name="cart"),
    #new
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

]
