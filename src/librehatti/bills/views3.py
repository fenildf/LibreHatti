from django.shortcuts import render
from django.http import HttpResponseRedirect 
from librehatti.catalog.models import PurchaseOrder, PurchasedItem
from librehatti.bills.models import *
from django.contrib.auth.models import User
import useraccounts
from django.db.models import Sum
import forms

def confirm(request):
    if request.method=='POST':
        a = ConfirmForm(request.POST)
        if a.is_valid():
            cd = a.cleaned_data
            quote_item = cd['quote_item'] 
            quote_qty = cd['quote_qty']
            obj = QuotedItem(quote_item=quote_item,quote_qty=quote_qty)
            obj.save()
 	    return HttpResponseRedirect('bills/confirm/')



    else:
             a = ConfirmForm()		
    return render(request,'bills/confform.html',{'form':a})

def generate(request):

    quoted_order = PurchaseOrder.objects.get(pk=1)
    quoted_item = PurchasedItem.objects.filter(pk=1).values_list('item__name' ,
		'qty' , 'price')	
    total = PurchasedItem.objects.filter(id=1).aggregate(Sum('price')).get('price__sum', 0.00)
    return render(request, 'bills/bills.html',{ 'quoted_order' : quoted_order, 
                     'quoted_item' : quoted_item , 'total_cost': total} )	 
  
	

