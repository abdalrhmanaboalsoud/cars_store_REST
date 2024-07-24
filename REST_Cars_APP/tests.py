from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Car

class CarTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        testuser1 = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        
        # Create a test car
        test_car = Car.objects.create(
            brand="Toyota",
            model="Corolla",
            price=20000,
            is_bought=True,
            buy_time=timezone.now(),
            buyer_id=testuser1
        )

    def test_str_method(self):
        # Retrieve the test car
        car = Car.objects.get(id=1)
        
        # Construct the expected string representation
        expected_str = f"{car.brand} {car.model} has bought by {car.buyer_id} for {car.price}$"
        
        # Assert the string representation matches
        self.assertEqual(str(car), expected_str)

