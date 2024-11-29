from django.shortcuts import get_object_or_404, redirect, render

from .models import Manufacturer, Product
from utils.aws_utils import AWSManager


# List all manufacturers
def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})

# Add a new manufacturer
def add_manufacturer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        company_name = request.POST['company_name']
        location = request.POST['location']
        Manufacturer.objects.create(name=name, email=email, phone=phone, company_name=company_name, location=location)
        return redirect('manufacturer_list')
    return render(request, 'add_manufacturer.html')

# List products for a specific manufacturer
def product_list(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, id=manufacturer_id)
    products = manufacturer.products.all()
    return render(request, 'product_list.html', {'manufacturer': manufacturer, 'products': products})

# Add a product
def add_product(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, id=manufacturer_id)
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        description = request.POST.get('description', '')
        Product.objects.create(manufacturer=manufacturer, name=name, price=price, stock=stock, description=description)
        return redirect('product_list', manufacturer_id=manufacturer.id)
    return render(request, 'add_product.html', {'manufacturer': manufacturer})

def some_view(request):
    aws = AWSManager()
    
    # Send SNS notification
    aws.send_sns_notification("New order received!")
    
    # Send message to SQS
    aws.send_sqs_message("Process order #123")
    
    # Upload file to S3
    if request.FILES.get('document'):
        file_url = aws.upload_file_to_s3(
            request.FILES['document'],
            f"documents/{request.FILES['document'].name}"
        )
