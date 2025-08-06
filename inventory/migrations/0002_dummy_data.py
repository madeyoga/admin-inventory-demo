from django.db import migrations


def create_dummy_data(apps, schema_editor):
    Category = apps.get_model('inventory', 'Category')
    Product = apps.get_model('inventory', 'Product')
    StockMovement = apps.get_model('inventory', 'StockMovement')

    # Create categories
    electronics = Category.objects.create(name='Electronics')
    books = Category.objects.create(name='Books')
    clothing = Category.objects.create(name='Clothing')

    # Create products
    laptop = Product.objects.create(
        name='Laptop',
        sku='LAP123',
        category=electronics,
        stock=10,
        price=1200.00
    )
    novel = Product.objects.create(
        name='Novel',
        sku='NOV456',
        category=books,
        stock=50,
        price=15.99
    )
    tshirt = Product.objects.create(
        name='T-Shirt',
        sku='TSH789',
        category=clothing,
        stock=100,
        price=9.99
    )

    # Create stock movements
    StockMovement.objects.create(
        product=laptop,
        type='IN',
        quantity=10
    )
    StockMovement.objects.create(
        product=novel,
        type='IN',
        quantity=50
    )
    StockMovement.objects.create(
        product=tshirt,
        type='IN',
        quantity=100
    )
    StockMovement.objects.create(
        product=laptop,
        type='OUT',
        quantity=2
    )


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dummy_data, reverse_code=migrations.RunPython.noop),
    ]
