from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="GreekSalad", price=12.50, inventory=25)
        Menu.objects.create(title="Bruschetta", price=8.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_item(self):
        item = Menu.objects.get(Title="GreekSalad")
        response = self.client.get(f'/restaurant/menu/{item.pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, MenuSerializer(item).data)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_booking_requires_token(self):
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_and_list_booking_with_token(self):
        user = User.objects.create_user(username='ana', password='Str0ng!pass42')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        payload = {
            'Name': 'Ana',
            'No_of_guests': 3,
            'BookingDate': '2026-12-01T19:00:00Z',
        }
        created = self.client.post('/restaurant/booking/tables/', payload, format='json')
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        listing = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(listing.status_code, status.HTTP_200_OK)
        self.assertEqual(len(listing.data), 1)
