# Little Lemon API

Capstone project for the Meta Back-End Developer course. It's a Django + Django REST Framework backend for the Little Lemon restaurant. It serves a simple home page, exposes a Menu API and a Table Booking API, stores data in MySQL, and uses token authentication for users.

## What's in it

- Home page rendered from a Django template with static CSS and images
- Menu API (list, create, update, delete menu items)
- Booking API (same operations for table reservations, login required)
- User registration and token login using Djoser and DRF's token auth
- Unit tests for the Menu and Booking models and views (`littlelemon/tests/test_models.py`, `test_views.py`)

## API paths to test

| Path | Methods | Notes |
|---|---|---|
| `/restaurant/` | GET | Home page |
| `/restaurant/menu/` | GET, POST | List or add menu items |
| `/restaurant/menu/<id>/` | GET, PUT, PATCH, DELETE | Single menu item (works with or without the trailing slash) |
| `/restaurant/booking/tables/` | GET, POST | Needs a token |
| `/restaurant/booking/tables/<id>/` | GET, PUT, PATCH, DELETE | Needs a token |
| `/auth/users/` | GET, POST | POST registers a new user |
| `/auth/token/login/` | POST | Returns an auth token |
| `/auth/token/logout/` | POST | Invalidates the token |
| `/restaurant/api-token-auth/` | POST | Alternative way to get a token |

## Running it locally

You'll need Python 3 and a MySQL server running on `127.0.0.1:3306`.

```bash
git clone <repo-url>
cd meta-backend-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create the database:

```sql
CREATE DATABASE LittleLemon;
```

The settings use the `root` user with an empty password. If yours has a password, change it under `DATABASES` in `littlelemon/littlelemon/settings.py`.

Then run the migrations, create a user and start the server:

```bash
cd littlelemon
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The site is then available at http://127.0.0.1:8000/restaurant/.

## Trying the API in Insomnia

1. Send a POST to `/auth/token/login/` with `username` and `password` in the body. You'll get back an `auth_token`.
2. For requests to the booking endpoints, open the Auth tab, pick Bearer Token, paste the token and set the prefix to `Token`. You can also add the header `Authorization: Token <your token>` yourself.
3. Send GET or POST requests to `/restaurant/booking/tables/`.

Without a token, the booking endpoints return 401.

## Tests

```bash
cd littlelemon
python manage.py test
```
