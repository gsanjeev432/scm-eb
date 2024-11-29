from customer.models import Customer
from django.shortcuts import get_object_or_404, redirect, render
from manufacturer.models import Product

from .models import Order


# List all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

# Create a new order
def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST['customer']
        product_id = request.POST['product']
        quantity = request.POST['quantity']
        
        customer = get_object_or_404(Customer, id=customer_id)
        product = get_object_or_404(Product, id=product_id)
        
        # Create the order
        Order.objects.create(
            customer=customer,
            product=product,
            quantity=quantity,
            status='Placed'
        )
        return redirect('order_list')
    
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'create_order.html', {'customers': customers, 'products': products})

# View order details
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_details.html', {'order': order})

# Update the status of an order
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = request.POST['status']
        order.save()
        return redirect('order_details', order_id=order.id)
    
    return render(request, 'update_order_status.html', {'order': order})
