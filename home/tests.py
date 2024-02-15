from django.test import TestCase, Client
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class APITest(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()

        user = User.objects.create(email='test@gmail.com', password='123456', name='test')
        refresh_token = RefreshToken.for_user(user)
        token = refresh_token.access_token
        self.auth_header = f"Bearer {token}"
        return super().setUp()

    def test_unauthenticated_request(self):

        response = self.client.get('/products/')
        self.assertEquals(response.status_code, 401)

        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, 401)

        

    def test_authenticated_request(self):
        
        response = self.client.get('/products/', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/tags/', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, 200)