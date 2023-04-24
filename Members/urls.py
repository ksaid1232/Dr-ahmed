from . import views
from django.urls import path


urlpatterns = [
    path("login_users/", views.Login_customer, name='Members'),
    path("signup_users/", views.Register_customer, name="register"),
    path("logout_users/", views.Logoutcustomer, name="logout"),


]
