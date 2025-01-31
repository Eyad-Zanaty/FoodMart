from django.shortcuts import redirect, render
from .models import Market, Customers, Cart
from django.db.models import Sum
# Create your views here.

def landpage(request):
    prod= Market.objects.all()
    user= Customers.objects.get(name= request.user)
    carts= Cart.objects.all()
    if request.method== 'POST' and "add_to_cart" in request.POST:
        product_id= request.POST.get("product_id")
        quantity = request.POST.get("quantity", 1) 
        products= Market.objects.get(id= product_id)
        cart = Cart.objects.create(product=products, number=quantity, price= float(products.price) * int(quantity))
        user.save()
        cart.save()
        return redirect('home:landpage')
    total_price = Cart.objects.aggregate(total_price=Sum('price'))['total_price'] or 0 or 0
    context= {'prod': prod, 'user': user, 'carts': carts, 'total_price': total_price}
    return render(request, 'home/home.html', context)