## Students

- Javadagha Salmanov
- Adil Valizada
- Gulandam Saidbayli
- Cafar Abbasov
- Nuran Amirkhanov
- Chingiz Gurbanov
- Eljan Rustamov

This Django project appears to encompass functionalities related to an e-commerce platform, with a focus on customer interactions and product management.

## Customer App

#### Models
- **Customer**: Represents a customer with fields derived from the [`User`](.virtualenvs/ecommerce-shop-site-lesson-project-7M1L-YYh/Lib/site-packages/django/contrib/auth/models.py) model and additional attributes specific to a customer.
- **Wish**: A model to represent customer wishes or wishlists.
- **BasketItem**: Items that are added to a customer's shopping basket.
- **Coupon**: Represents discount coupons.
- **Order**: Details of customer orders.
- **OrderCoupon**: Association between orders and coupons.
- **Purchase**: Represents completed purchases.
- **Contact**: Stores contact information.
- **PasswordReset**: For managing password reset requests.
- **BulkMail**: Likely used for sending bulk emails to customers.

#### Forms
- **RegisterForm**: A form for user registration.
- **ContactForm**: A form for contact information, based on the [`Contact`](customer/models.py) model.
- **CheckoutForm**: A form used during the checkout process.
- **ResetPasswordEmailForm**: For initiating a password reset via email.
- **ResetPasswordForm**: For completing the password reset process.

#### Views
- **ContactView**: A class-based view for contact functionality.
- **login_view**: Function-based view for handling login.
- **logout_view**: Handles user logout.
- **register**: Manages user registration.
- **wishlist**: (Commented out) Would display a user's wishlist.

## E-commerce App

#### Models
- **Size**, **Color**: Attributes for products.
- **Category**: Product categorization.
- **Campaign**: Represents marketing campaigns.
- **Product**: Core model representing products.
- **ProductImage**: Images associated with products.
- **Review**: Customer reviews for products.

#### Views
- **home**: Displays the homepage with featured products, campaigns, and categories.
- **ProductListView**: A class-based view for listing products with pagination.

### General Functionality Overview

- **Product Management**: The platform allows for the management of products, including details like size, color, and categories. Products can be featured in campaigns and have associated images and reviews.
- **Customer Interaction**: Customers can register, login/logout, and contact the platform. There's functionality for managing wishlists, shopping baskets, and orders, including the application of coupons.
- **Security**: The project includes mechanisms for password reset and uses Google's reCAPTCHA for form submissions to prevent spam.

This documentation provides a high-level overview of the project's functionalities based on the provided code excerpts. For a more detailed understanding, one would need to review the full source code.

## Setup

This documentation outlines the setup process for the Django project configured in [`settings.py`](2%7D%5D"shop-site-lesson-project\shop\settings.py). Follow these steps to configure your environment correctly.

## Prerequisites

- Python 3.8 or higher
- Django 4.1.3
- PostgreSQL
- An SMTP server for email sending capabilities

## Environment Variables

The project relies on environment variables for configuration. Set the following variables in your environment:

- [`SECRET_KEY`](shop/settings.py): A secret key for Django. Generate one using Django's `get_random_secret_key()` function.
- [`DEBUG`](shop/settings.py): Set to `True` for development, `False` for production.
- [`ALLOWED_HOSTS`](shop/settings.py): A comma-separated list of hosts/domains the app can serve. Example: `localhost,127.0.0.1`
- Database Configuration:
  - `DB_NAME`: The name of your PostgreSQL database.
  - `DB_USER`: The username for your database.
  - `DB_PASSWORD`: The password for your database user.
  - `DB_HOST`: The host of your database, typically `localhost` for a local setup.
  - `DB_PORT`: The port your database listens on, usually `5432` for PostgreSQL.
- Email Configuration:
  - [`EMAIL_HOST`](shop/settings.py): The host of your SMTP server.
  - [`EMAIL_PORT`](shop/settings.py): The port your SMTP server uses.
  - [`EMAIL_HOST_USER`](shop/settings.py): The username for your SMTP server.
  - [`EMAIL_HOST_PASSWORD`](shop/settings.py): The password for your SMTP server.
  - `EMAIL_USE`: Set to `SSL` or `TLS` depending on your SMTP server's configuration.
- Security Settings:
  - [`SECURE_HSTS_SECONDS`](shop/settings.py): The number of seconds HTTP Strict Transport Security will be enforced.
  - [`SECURE_SSL_REDIRECT`](shop/settings.py): Set to `True` to redirect all non-HTTPS requests to HTTPS.
  - [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](shop/settings.py): Set to `True` to include subdomains in the HSTS policy.
  - [`SESSION_COOKIE_SECURE`](shop/settings.py): Set to `True` to make the session cookie secure (only sent over HTTPS).
  - [`CSRF_COOKIE_SECURE`](shop/settings.py): Set to `True` to make the CSRF cookie secure.
  - [`SECURE_HSTS_PRELOAD`](shop/settings.py): Set to `True` to allow preloading of the site's HSTS policy.

## Database Setup

Ensure PostgreSQL is installed and running. Create a database that matches the `DB_NAME` environment variable you've set.

## Running the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Apply migrations to create the database schema:

```bash
python manage.py migrate
```

3. Run the development server:

```bash
python manage.py runserver
```

## Docker Configuration

This project is configured to run with Docker, simplifying the setup and deployment processes. Here's how to get started with Docker:

### Prerequisites

- Docker
- Docker Compose

### Running the Project with Docker

1. **Build the Docker Images**

   Navigate to the project root directory and run the following command to build the Docker images specified in the `docker-compose.yml` file:

   ```bash
   docker-compose build
   ```
2. **Start the Containers**

    After building the images, start the containers with:
    ```bash
    docker-compose up
    ```
    This command starts all the services defined in docker-compose.yml. The backend service will be accessible at http://localhost:8000, and the database service uses a volume shop_db_data to persist data.

3. **Environment Variables**

      The Docker configuration uses an .env file to set environment variables for the containers. Ensure you have an .env file at the root of your project with the necessary variables. Refer to .env.example for an example configuration.

      Database Initialization

      With the containers running, you may need to apply database migrations. You can do this by executing the following command:

## Static and Media Files

- Static files are served from the `staticfiles/` directory and configured under `STATIC_URL` and `STATIC_ROOT`.
- Media files are uploaded to and served from the `media/` directory, configured under `MEDIA_URL` and `MEDIA_ROOT`.

## Internationalization

The project is configured for multiple languages with default language set to English. Translations are located in the `locale` directory.

## Security

Review the security settings section and ensure appropriate values are set before deploying to production.

## Email Configuration

Configure the SMTP settings according to your email service provider to enable email sending capabilities.

## Caching

The project uses file-based caching configured under the `CACHES` setting. Ensure the cache directory is writable by the web server.

---


## Unit Testing

This project uses Django's built-in `TestCase` class for unit testing. Tests are organized by application within the project structure. Here's how to run and write tests for the project:

### Running Tests

To run all tests in the project, execute the following command from the root directory:

```sh
python manage.py test
```

To run tests for a specific application, specify the application name:

```sh
python manage.py test customer
python manage.py test ecommerce
```

### Writing Tests

Tests are defined in the `tests.py` file within each application directory. Each test case class should inherit from `django.test.TestCase`.

#### Example Test Case

Below is an example of a test case for the `Product` model in the `ecommerce` application:

```python
from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=10.00)

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product)
        self.assertEqual(product.price, 10.00)
```

This test case creates a [`Product`](ecommerce/models.py) instance in the [`setUp`](ecommerce/tests.py) method and then tests that the product was created with the correct price.

### Best Practices

- Group related tests into the same [`TestCase`](virtualenvs/ecommerce-shop-site-lesson-project-7M1L-YYh/Lib/site-packages/django/test/testcases.py) class.
- Use the [`setUp`](ecommerce/tests.py) method to create common test data for each test method.
- Use descriptive names for your test methods to clearly indicate what they test.

For more information on testing in Django, refer to the [official Django testing documentation](https://docs.djangoproject.com/en/stable/topics/testing/).


## Admin Panel
The project's Django admin panel is configured through customizations in the [`admin.py`]("customer\admin.py) files located in the [`customer`](mmerce\lesson\customer) and [`ecommerce`](mmerce\lesson\ecommerce) applications. Below is a summary of these configurations:

### Customer App Admin Configuration ([`customer/admin.py`]("customer\admin.py))

- **Models Registered Directly:**
  - [`Customer`]("customer/models.py)
  - [`Wish`]("customer/models.py)
  - [`BascetItem`]("customer/models.py)
  - [`Contact`]("customer/models.py)
  - [`Purchase`]("customer/models.py)
  - [`Coupon`]("customer/models.py)
  - [`OrderCoupon`]("customer/models.py)
  - [`PasswordReset`]("customer/models.py)
  - [`BulkMail`]("customer/models.py)

- **Custom Admin Classes:**
  - [`OrderAdmin`]("customer/admin.py): Configures the admin interface for the [`Order`]("customer/models.py) model. It uses two inline classes, [`OrderCouponInline`]("customer/admin.py) and [`PurchaseInline`]("customer/admin.py), to display related [`OrderCoupon`]("customer/models.py) and [`Purchase`]("customer/models.py) instances within the same page as the [`Order`]("customer/models.py) instance.
    - [`OrderCouponInline`](D "customer/admin.py): Displays [`OrderCoupon`](D "customer/models.py) instances in a tabular inline format. It is set to not allow adding extra instances directly from the [`Order`](D "customer/models.py) admin page ([`extra = 0`](D "customer/admin.py)).
    - [`PurchaseInline`](D "customer/admin.py): Displays [`Purchase`](D "customer/models.py) instances in a stacked inline format, also without allowing extra instances to be added directly ([`extra = 0`](D "customer/admin.py)).

### Ecommerce App Admin Configuration ([`ecommerce/admin.py`]("ecommerce\admin.py))

- **Models Registered Directly:**
  - [`Size`]("ecommerce/models.py)
  - [`Color`]("ecommerce/models.py)
  - [`Category`]("ecommerce/models.py)
  - [`Campaign`]("ecommerce/models.py)
  - [`ProductImage`]("ecommerce/models.py)

- **Custom Admin Classes:**
  - [`ProductAdmin`]("ecommerce/admin.py): Customizes the admin interface for the [`Product`]("ecommerce/models.py) model. It specifies [`readonly_fields`]("ecommerce/admin.py) to include `id`, `slug`, and `created`. It also includes two inline classes, [`ProductImageInline`]("ecommerce/admin.py) and [`ReviewInline`]("ecommerce/admin.py), to display related [`ProductImage`]("ecommerce/models.py) and [`Review`]("ecommerce/models.py) instances within the same page as the [`Product`]("ecommerce/models.py) instance.
    - [`ProductImageInline`]("ecommerce/admin.py): Configures a tabular inline view for [`ProductImage`]("ecommerce/models.py) instances. It includes `image`, `image_tag`, and `order` fields, with `image_tag` being read-only. It allows adding one extra [`ProductImage`]("ecommerce/models.py) instance directly from the [`Product`]("ecommerce/models.py) admin page ([`extra = 1`]("customer/admin.py)).
    - [`ReviewInline`]("ecommerce/admin.py): The configuration for this inline class is not provided in the excerpt, but it is implied to be similar in purpose to [`ProductImageInline`]("ecommerce/admin.py), allowing [`Review`]("ecommerce/models.py) instances to be managed directly from the [`Product`]("ecommerce/models.py) admin page.

These configurations enhance the Django admin interface by allowing detailed management of related models directly from the admin pages of their parent models, improving the efficiency of administrative tasks.