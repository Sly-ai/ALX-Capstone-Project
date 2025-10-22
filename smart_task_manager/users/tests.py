from django.test import TestCase
from rest_framework.test import APIClient
from .models import User

# Create your tests here.
class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='pass')
        self.client.force_authenticate(user=self.superuser)

    def test_create_user(self):
        response = self.client.post('/api/users/', {'username': 'test', 'email': 'test@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 201)