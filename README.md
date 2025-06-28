
# 🛒 Django E-Commerce App (Template-Based)

This is a minimal e-commerce web application built using **Django** with **Django Templates** (no React, no Docker). It supports essential features like product listing, cart functionality, and order placement.

---

##  Features

-  User registration and login (using Django Auth)
-  Product list and detail view
-  Add to cart /  remove from cart
-  Place orders with address & phone number
-  Admin dashboard to manage products/orders
-  Server-side rendering using Django templates

---

##  Tech Stack

- Backend: Django (Python)
- Frontend: Django Templates (HTML, CSS)
- Database: SQLite3 (default)

---

##  Project Structure

ecommerce/
├── cart/
├── order/
├── product/
├── store/ # User login/logout/registration
├── templates/
│ ├── base.html
│ ├── home.html
├── ecommerce/ # Main settings
├── db.sqlite3
├── manage.py
└── seed.py # Add dummy products


---

##  Setup Instructions

### 1.  Clone the Repository

```bash
git clone https://github.com/Ranikannan264/holy_rock.git
cd ecommerce
```

### 2.  Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3.  Install Dependencies
Create a `requirements.txt` file with the following:
```txt
# Core
Django=4.2
djangorestframework=3.14.0
djangorestframework-simplejwt=5.3.0

# Celery & Redis (for background tasks like sending order confirmation)
celery>=5.3.0
redis>=5.0.1

# CORS (if needed for API)
django-cors-headers>=4.3.0

Then install:
```bash
pip install -r requirements.txt
```


### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5.  Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6.  (Optional) Seed Products
```bash
python seed.py
```

### 7.  Run the Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000
✅ Usage

   - Go to /admin to add/edit products manually.
   - Visit homepage / to view products.
   - Go to /cart/add/5/ to add products.
   - Go to /cart/view/ to view your cart.
   - Place an order via /order/place/.
----

 ### User Accounts

   - Default Django Auth system used
   - Visit /accounts/login/ and /logout/
----

### Sample Test Data

   - To add dummy products, run the seed.py file:

   - python seed.py
----

### It adds basic products to the database.
## Admin Panel

Use your superuser credentials to access:

http://127.0.0.1:8000/admin/
----
### Manage:
   - Users
   - Products
   - Orders
   - CartItems
----
### Notes
    - This app is for learning/demo purposes.
    - No payment gateway is integrated.
    - Use Django’s inbuilt auth system for login/logout.
----

##  API Documentation

API details including available endpoints, request/response samples, and authentication instructions are available in the PDF below:

[Download API Documentation](docs/django_ecommerce_api_doc.pdf)

---

## License
This project is licensed for HOLY ROCK & GREEN FLAG internal development and educational purpose

