from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from GenrateInvoice.models import CustomerDetails
from GenrateInvoice.models import ProductInfo
from GenrateInvoice.forms import CustomerDetailsForm
from GenrateInvoice.forms import ProductInfoForm
from GenrateInvoice.models import InvoiceNO

from datetime import date 
  
# Create your views here.


def uploadCust(request):
    if request.method == "POST":
        if 'CustomerSubmit' in request.POST:
            custform = CustomerDetailsForm(request.POST)
            if custform.is_valid():
                try:
                    custform.save()
                    return redirect('/details')
                except :
                    pass
        else:
            prodform = ProductInfoForm(request.POST)
            if prodform.is_valid():
                try:
                    prodform.save()
                    return redirect('/details')
                except:
                    pass

    else:
        custform = CustomerDetailsForm()
        prodform = ProductInfoForm()
        return render(request,"upload.html",{'cust': custform ,'prod': prodform})



def details(request):
    custdetails = CustomerDetails.objects.all()
    proddetails  =  ProductInfo.objects.all()
    return render(request ,"info.html" ,{'cust': custdetails , 'prod': proddetails})

billNo = 1
def invoice(request):
    if request.method == "POST":
        custname = request.POST.get('custname')
        print(custname)
        custinfo= CustomerDetails.objects.get(name=custname)
        selectedprod = request.POST.getlist('pname')
        print(selectedprod)
        rate = (request.POST.getlist('rate'))
        print(rate)
        quantity = (request.POST.getlist('quantity'))
        print(quantity)
        state = request.POST.get('state')
        print(state)
        print(type(state))
        total = []
        size = len(rate)
        i =0
        while (i < len(rate)):
            mul = int(rate[i]) * int(quantity[i])
            total.append(mul)
            i = i + 1
        print(total)
        sum = 0
        for t in total:
            sum = sum + t
        print (sum)
        today = date.today()
        print(today)

        b = InvoiceNO.objects.get(id = 1)
        billNo=(b.billno)
        c = b.billno+1
        b.billno = c
        b.save()
        if (state == 'state'):
            cgst = 9
            sgst = 9
            amount = sum + 0.18*sum
            rest ={
                "cust":custinfo ,
                "check":1,
                "cgst":cgst ,
                "sgst":sgst ,
                "sum":sum ,
                "amt":amount , 
                "date":today,
                "BillNo":billNo,
                "size":size,
                "prodinfo":zip(selectedprod,rate,quantity)
                }
            print(rest)
            
            return render(request,"invoice.html",{"info":rest})
        else:
            print("el")
            igst = 18
            amount = sum + 0.18*sum
            rest ={
                "cust":custinfo ,
                "check":2,
                "igst":igst,
                "sum":sum ,
                "amt":amount , 
                "date":today,
                "BillNo":billNo,
                "size":size,
                "prodinfo":zip(selectedprod,rate,quantity)
                }
            
            
            print(rest)
            return render(request,"invoice.html",{"info":rest})

            
    


