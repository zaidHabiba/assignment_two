from django.test import Client
from django.test import TestCase

from app.models import User


class TestLogin(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="zaid", is_superuser=True)
        user1.set_password("zaid")
        user1.save()
        user2 = User.objects.create(username="alice")
        user2.set_password("alice")
        user2.save()

    def test_login(self):
        client = Client()
        response = client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog")
        print(response)

    def test_redirect_not_login(self):
        client = Client()
        response = client.get('/catalog/books/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/login/?next=/catalog/books/")
        print(response)

    def test_forbidden(self):
        client = Client()
        client.post('/catalog/login/', {'username': 'alice', 'password': 'alice'})
        response = client.get('/catalog/books/')
        self.assertEqual(response.status_code, 403)

    def test_success(self):
        client = Client()
        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_request_permissions(self):
        client = Client()
        client.post('/catalog/login/', {'username': 'alice', 'password': 'alice'})
        response = client.get('/catalog/books/')
        self.assertEqual(response.status_code, 403)
        response = client.post('/catalog/book/add/')
        self.assertEqual(response.status_code, 403)

        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.post('/catalog/book/add/', {"name": "alice", "summary": "xxxxxxxx"})
        self.assertEqual(response.status_code, 200)
        response = client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_author_request_permissions(self):
        client = Client()

        client.post('/catalog/login/', {'username': 'alice', 'password': 'alice'})
        response = client.post('/catalog/authors/')
        self.assertEqual(response.status_code, 403)
        response = client.get('/catalog/author/add/')
        self.assertEqual(response.status_code, 403)

        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.post('/catalog/author/add/',
                               {"name": "alice", "nationality": "xxxxxxxx", "birth_place": "xxxxxxxx"})
        self.assertEqual(response.status_code, 200)
        response = client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_language_request_permissions(self):
        client = Client()

        client.post('/catalog/login/', {'username': 'alice', 'password': 'alice'})
        response = client.get('/catalog/languages/')
        self.assertEqual(response.status_code, 403)
        response = client.post('/catalog/language/add/')
        self.assertEqual(response.status_code, 403)

        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.post('/catalog/language/add/', {"language": "english"})
        self.assertEqual(response.status_code, 302)  # Redirect to catalog/languages/
        self.assertRedirects(response, "/catalog/languages/")
        response = client.get('/catalog/languages/')
        self.assertEqual(response.status_code, 200)

    def test_genre_request_permissions(self):
        client = Client()

        client.post('/catalog/login/', {'username': 'alice', 'password': 'alice'})
        response = client.get('/catalog/genres/')
        self.assertEqual(response.status_code, 403)
        response = client.post('/catalog/genre/add/')
        self.assertEqual(response.status_code, 403)

        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.post('/catalog/genre/add/', {"genre": "x113a"})
        self.assertEqual(response.status_code, 302)  # Redirect to catalog/genres/
        self.assertRedirects(response, '/catalog/genres/')
        response = client.get('/catalog/genres/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        client = Client()
        client.post('/catalog/login/', {'username': 'zaid', 'password': 'zaid'})
        response = client.post('/catalog/logout/')
        self.assertEqual(response.status_code, 200)
