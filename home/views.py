from django.conf import settings
from django.shortcuts import redirect, render
from .models import Market, Customers, Cart
from django.db.models import Sum
from django.core.mail import send_mail
from .form import SubscriptionForm
# Create your views here.

def landpage(request):
    prod= Market.objects.all()
    user= Customers.objects.get(name= request.user)
    carts= Cart.objects.all()
    total_price = Cart.objects.aggregate(total_price=Sum('price'))['total_price'] or 0
    form = SubscriptionForm(instance=user)
        
    if request.method== 'POST' and "add_to_cart" in request.POST:
        product_id= request.POST.get("product_id")
        quantity = request.POST.get("quantity", 1) 
        products= Market.objects.get(id= product_id)
        cart = Cart.objects.create(product=products, number=quantity, price= float(products.price) * int(quantity))
        user.save()
        cart.save()
    
    
    if request.method== 'POST' and 'subscribe' in request.POST:
        form = SubscriptionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            Name=request.POST['name']
            email=request.POST['email']
            send_mail(
                'Discount',
                f'{Name} has got the discount',
                [settings.EMAIL_HOST_USER],
                email,
            )
            return redirect('home:landpage')
        else:
            form.save()
            
    context= {'prod': prod, 'user': user, 'carts': carts, 'total_price': total_price, 'form': form}
    return render(request, 'home/home.html', context)