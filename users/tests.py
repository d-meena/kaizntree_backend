from django.test import TestCase, Client
from users.models import User
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

class ModelTest(TestCase):

    def test_user_email_validation(self):

        with self.assertRaises(ValidationError):
            user = User.objects.create(email='abcd', password='123456')
            user.full_clean()


    
    def test_user_creation(self):
        User.objects.create(email='abcd@gmail.com', password='123456')


class APITest(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.user_data  = {
            "email": "random@gmail.com",
            "name": "random2",
            "password": "random@234",
            "confirm_password": "random@234"
        }
        return super().setUp()
    
    def test_email_validity_checks(self):

        data = self.user_data.copy()
        data["email"] = "notanemail.com"
        response = self.client.post('/auth/register/', data,format='json')
        self.assertEquals(response.status_code, 400)
        self.assertIsNotNone(response.json().get("email"))
        self.assertIsNone(response.json().get("name"))
        self.assertIsNone(response.json().get("password"))



    def test_password_validity_check(self):

        data = self.user_data.copy()
        data["password"] = "weak"
        response = self.client.post('/auth/register/', data,format='json')
        self.assertEquals(response.status_code, 400)
        self.assertIsNone(response.json().get("email"))
        self.assertIsNone(response.json().get("name"))
        self.assertIsNotNone(response.json().get("password"))

        data = self.user_data.copy()
        data["confirm_password"] = "notthesame@password"
        response = self.client.post('/auth/register/', data,format='json')
        self.assertEquals(response.status_code, 400)
        self.assertIsNone(response.json().get("email"))
        self.assertIsNone(response.json().get("name"))
        self.assertIsNotNone(response.json().get("password"))



    def test_name_validity_check(self):

        data = self.user_data.copy()
        data.pop("name")
        response = self.client.post('/auth/register/', data,format='json')
        self.assertEquals(response.status_code, 400)
        self.assertIsNone(response.json().get("email"))
        self.assertIsNotNone(response.json().get("name"))
        self.assertIsNone(response.json().get("password"))


    def test_registration_login(self):

        response = self.client.post('/auth/register/',self.user_data,format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user_data.get("email"), response.json().get("email"))
        self.assertEqual(self.user_data.get("name"), response.json().get("name"))

        refresh_token = RefreshToken(response.json().get("tokens").get("refresh"))
        refresh_token.verify()
        self.assertEquals(refresh_token.get('user_id'), self.user_data.get("email"))

        data = {
            "email": self.user_data.get("email"),
            "password": self.user_data.get("password")
        }

        response = self.client.post('/auth/login/',data,format="json")
        self.assertEquals(response.status_code,200)







    