from django.shortcuts import render, redirect,get_object_or_404
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from .tasks import send_order_confirmation_email

@login_required
def place_order(request):
    if request.method == 'POST':
        # Get cart items for user that are not yet ordered
        items = CartItem.objects.filter(user=request.user, is_ordered=False)

        if not items.exists():
            return render(request, 'error.html', {'message': 'Your cart is empty.'})

        # Validate input
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        if not address or not phone:
            return render(request, 'error.html', {'message': 'Address and phone number are required.'})

        # Calculate total price
        total = sum(item.total_price for item in items)

        # Create the order
        order = Order.objects.create(
            user=request.user,
            address=address,
            phone=phone,
            total_price=total
        )

        # Transfer cart items to order items
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # Mark cart items as ordered
        items.update(is_ordered=True)
        
        send_order_confirmation_email.delay(request.user.email, order.id)

        return redirect('order_success', order_id=order.id)

    return redirect('checkout')  # fallback if not POST

def order_success(request,order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_success.html',{'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def checkout_view(request):
    items = CartItem.objects.filter(user=request.user, is_ordered=False)

    if not items.exists():
        return render(request, 'error.html', {'message': 'Your cart is empty.'})

    total = sum(item.total_price for item in items)

    return render(request, 'checkout.html', {
        'items': items,
        'total': total,
    })