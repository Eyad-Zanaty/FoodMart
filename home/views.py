from django.shortcuts import redirect, render
from .models import Market, Customers
from .form import CustomerForm
# Create your views here.

def landpage(request):
    prod= Market.objects.all()
    user= Customers.objects.get(id=1)
    if request.method== 'POST' and "add_to_cart" in request.POST:
        product_id= request.POST.get("product_id")
        product= Market.objects.get(id= product_id)
        user.purchase.add(product)
        user.save()
        print(user.purchase)
        return redirect('home:landpage')
    context= {'prod': prod, 'user': user}
    return render(request, 'home/home.html', context)