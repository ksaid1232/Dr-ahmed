from django.urls import path
from . import views

urlpatterns = [
    path("", views.Products_list),
    path('<int:id>/', views.Product_Details),
    path("featured/", views.Featured_list)

]
