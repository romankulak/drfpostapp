from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class AccountsTest(APITestCase):
    def setUp(self):
        self.test_pass = 'testpassword'
        self.test_user = User.objects.create_user(
            'testuser', 
            'test@example.com', 
            self.test_pass
        )
        self.create_url = reverse('user-list')
        self.get_jwt_url = reverse('token_obtain_pair')

    def test_create_user(self):
        data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password': 'testpassword2'
        }
        response = self.client.post(self.create_url , data)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_get_jwt(self):
        data = {
            'username': self.test_user.username,
            'password': self.test_pass
        }
        response = self.client.post(
            self.get_jwt_url, 
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)


class PostTest(APITestCase):
    def setUp(self):
        self.test_pass = 'testpassword'
        self.test_user = User.objects.create_user(
            'testuser', 
            'test@example.com', 
            self.test_pass
        )
        self.create_url = reverse('post-list')
        self.get_jwt_url = reverse('token_obtain_pair')
        self.token = self.client.post(
            self.get_jwt_url , 
            {
                'username': self.test_user.username,
                'password': self.test_pass
            }
        ).data
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token['access'])
        self.response = client.post(self.create_url , {
            'content': 'Test',
            'title': 'Title Test',
        })


    def test_post_create(self):
        data = {
            'content': 'Foo',
            'title': 'Bar',
        }
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token['access'])
        response = client.post(self.create_url , data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['title'], data['title'])
    
    def test_post_delete(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token['access'])
        response = client.delete(f'{self.create_url}{self.response.data["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_patch(self):
        title = 'patched'
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token['access'])
        response = client.patch(
            f'{self.create_url}{self.response.data["id"]}/', 
            {'title': title}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], title)
