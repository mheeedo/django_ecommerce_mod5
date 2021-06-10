from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('login/',auth_views.LoginView.as_view(template_name='store/login.html'),name='login'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('logout/',auth_views.LogoutView.as_view(template_name='store/logout.html'),name='logout'),
    path('register/',views.register,name='register'),

]