from django.urls import path
from GenrateInvoice import views

urlpatterns = [
    path('uploadCust',views.uploadCust,name="uploadCustomer"),
    path('details',views.details,name="details"),
    path('invoice',views.invoice,name="Invoice"),
    
]