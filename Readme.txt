Little Lemon Capstone Project — API Endpoints to Test
=====================================================

1. Static HTML Home Page:
   http://127.0.0.1:8000/restaurant/

2. Menu API Endpoints (GET, POST, PUT, DELETE):
   /restaurant/menu/
   /restaurant/menu/<id>/   (for example /restaurant/menu/1/)
   /restaurant/menu/items/

3. Table Booking API Endpoints (Requires Token Authentication - GET, POST, PUT, DELETE):
   /restaurant/booking/tables/
   /restaurant/booking/tables/<id>/   (for example /restaurant/booking/tables/1/)

4. User Registration & Token Authentication Endpoints (Djoser & DRF AuthToken):
   /auth/users/
   /auth/token/login/
   /auth/token/logout/
   /restaurant/api-token-auth/

5. Running Unit Tests:
   cd littlelemon
   python manage.py test
