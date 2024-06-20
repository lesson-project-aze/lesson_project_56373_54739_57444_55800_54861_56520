## Students
* Javadagha Salmanov
* Adil Valizada
* Gulandam Saidbayli
* Cafar Abbasov
* Nuran Amirkhanov
* Chingiz Gurbanov

# Setup Documentation

This documentation outlines the setup process for the Django project configured in [`settings.py`](2%7D%5D"d:\Users\Ujer\Desktop\labs\lesson-project-ecommerce\ecommerce-shop-site-lesson-project\shop\settings.py"). Follow these steps to configure your environment correctly.

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

This setup documentation is based on the `settings.py` file and should be adjusted according to your specific deployment and development needs.