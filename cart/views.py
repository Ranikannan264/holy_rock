from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from product.models import Product  
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user, is_ordered=False)
    total = sum(item.total_price for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product,is_ordered=False,)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('view_cart')

@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item.quantity = quantity
        item.save()
    return redirect('view_cart')

@login_required
def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')
