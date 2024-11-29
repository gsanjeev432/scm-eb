from django.shortcuts import get_object_or_404, redirect, render

from .models import RawMaterial, Supplier


# List all suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

# Add a new supplier
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        company_name = request.POST['company_name']
        location = request.POST['location']
        Supplier.objects.create(name=name, email=email, phone=phone, company_name=company_name, location=location)
        return redirect('supplier_list')
    return render(request, 'add_supplier.html')

# List raw materials for a specific supplier
def raw_materials_list(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    materials = supplier.materials.all()
    return render(request, 'raw_materials_list.html', {'supplier': supplier, 'materials': materials})

# Add raw material
def add_raw_material(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        name = request.POST['name']
        price_per_unit = request.POST['price_per_unit']
        available_quantity = request.POST['available_quantity']
        description = request.POST.get('description', '')
        RawMaterial.objects.create(supplier=supplier, name=name, price_per_unit=price_per_unit, available_quantity=available_quantity, description=description)
        return redirect('raw_materials_list', supplier_id=supplier.id)
    return render(request, 'add_raw_material.html', {'supplier': supplier})
