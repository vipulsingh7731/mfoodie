from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.db.models import Q
from .models import Menu, Order, orderItem


# Showing index page
def home(request):
    return render(request, template_name='DelivApp/home.html')


def orderplaced(request):
    return render(request, 'DelivApp/orderplaced.html', {})

# Showing Menu list to Customer


def restuarantMenu(request, pk=None):

    menu = Menu.objects.all()

    items = []
    for i in menu:
        temp = []
        temp.append(i.name)
        temp.append(i.price)
        temp.append(i.id)
        temp.append(i.quantity)

        items.append(temp)
    context = {
        'items'	: items,
    }
    return render(request, 'DelivApp/menu.html', context)


@login_required(login_url='/login/')
def checkout(request):
    if request.POST:
        addr = request.POST['address']
        ordid = request.POST['oid']
        Order.objects.filter(id=int(ordid)).update(delivery_addr=addr,
                                                   status=Order.ORDER_STATE_PLACED)
        return redirect('/orderplaced/')
    else:
        cart = request.COOKIES['cart'].split(",")
        print(cart)
        cart = dict(Counter(cart))
        print(cart.items())
        items = []
        totalprice = 0
        uid = User.objects.filter(username=request.user)
        oid = Order()
        oid.orderedBy = uid[0]
        for key, value in cart.items():
            item = []
            it = Menu.objects.filter(id=int(key))
            if len(it):
                oiid = orderItem()
                oiid.item_id = it[0]
                oiid.quantity = int(value)
                oid.save()
                oiid.ord_id = oid
                oiid.save()
                totalprice += int(value)*it[0].price
                item.append(it[0].name)
                it[0].quantity = it[0].quantity - value
                it[0].save()
                item.append(value)
                item.append(it[0].price*int(value))

            items.append(item)
        oid.total_amount = totalprice
        oid.save()
        context = {
            "items": items,
            "totalprice": totalprice,
            "oid": oid.id
        }
        return render(request, 'DelivApp/order.html', context)

