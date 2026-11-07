from django.test import TestCase
from django.utils import timezone
from restaurant.models import Booking, Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingTest(TestCase):
    def test_booking_str(self):
        booking = Booking.objects.create(
            Name="Ana", No_of_guests=4, BookingDate=timezone.now()
        )
        self.assertEqual(str(booking), "Ana")
