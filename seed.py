import os
import django
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from product.models import Product

# Create a test user if needed
user, created = User.objects.get_or_create(username='admin')
if created:
    user.set_password('adminpass')
    user.save()

products = [
    {"name": "T-shirt", "description": "Cotton t-shirt", "price": 499},
    {"name": "Jeans", "description": "Slim fit jeans", "price": 1299},
    {"name": "Sneakers", "description": "Running shoes", "price": 2999},
    {"name": "Backpack", "description": "School/Office backpack", "price": 999},
    {"name": "Watch", "description": "Digital wrist watch", "price": 1999},
    {"name": "Sunglasses", "description": "UV protected glasses", "price": 799},
    {"name": "Cap", "description": "Stylish baseball cap", "price": 299},
    {"name": "Jacket", "description": "Winter jacket", "price": 2499},
    {"name": "Shorts", "description": "Casual shorts", "price": 699},
    {"name": "Socks", "description": "Cotton socks (pack of 3)", "price": 199},
]

for p in products:
    Product.objects.create(name=p["name"], description=p["description"], price=p["price"], owner=user)

print("✅ 10 products added!")
