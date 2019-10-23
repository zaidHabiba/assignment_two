from django.test import Client
from django.test import TestCase


class TestLogin(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.post('/catalog/login/',
                                    {'username': 'zaid', 'password': 'zaid'})
        self.assertEqual(response.status_code, 302)

    def test_redirect_not_login(self):
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/login/?next=/catalog/books/")

    def test_forbidden(self):
        self.client.login(username="alice", password="alice")
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 403)

    def test_success(self):
        self.client.post('/catalog/login/', {'username': 'zaid',
                                             'password': 'zaid'})
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_request_permissions(self):
        self.client.login(username="alice", password="alice")
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/catalog/book/add/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/book/add/',
                                    {"name": "alice", "summary": "xxxxxxxx"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_author_request_permissions(self):
        self.client.login(username="alice", password="alice")
        response = self.client.post('/catalog/authors/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/catalog/author/add/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/author/add/',
                                    {"name": "alice",
                                     "nationality": "xxxxxxxx",
                                     "birth_place": "xxxxxxxx"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_language_request_permissions(self):
        self.client.login(username="alice", password="alice")
        response = self.client.get('/catalog/languages/')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/catalog/language/add/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/language/add/',
                                    {"language": "english"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/languages/")
        response = self.client.get('/catalog/languages/')
        self.assertEqual(response.status_code, 200)

    def test_genre_request_permissions(self):
        self.client.login(username="alice", password="alice")
        response = self.client.get('/catalog/genres/')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/catalog/genre/add/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/genre/add/',
                                    {"genre": "x113a"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/catalog/genres/')
        response = self.client.get('/catalog/genres/')
        self.assertEqual(response.status_code, 200)

    def test_book_instance_request_permissions(self):
        self.client.login(username="alice", password="alice")
        response = self.client.get('/catalog/book-instances/')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/catalog/book-instance/add/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/book-instance/add/',
                                    {"status": "Maintenance",
                                     "due_book_date": "2000-2-3"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/catalog/book-instances/')
        self.assertEqual(response.status_code, 200)

    def test_book_add(self):
        self.client.login(username="zaid", password="zaid")

        response = self.client.post('/catalog/book/add/',
                                    {"name": "Java",
                                     "summary": "121 214 a5sd ad45a",
                                     "genre": "1",
                                     "language": "1",
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/books/")

    def test_book_instance_add(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/book-instance/add/',
                                    {"status": "M",
                                     "due_book_date": "2000-1-4",
                                     "book": "1",
                                     "person": "1",
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/book-instances/")

    def test_author_add(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/author/add/',
                                    {"name": "Zaid",
                                     "birth_date": "2000-1-5",
                                     "death_date": "2000-1-5",
                                     "nationality": "aaa bbb",
                                     "birth_place": "fff sss",
                                     "books": "1"
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/authors/")

    def test_language_add(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/language/add/',
                                    {"language": "English"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/languages/")

    def test_genre_add(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.post('/catalog/genre/add/',
                                    {"genre": "aaaa"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/genres/")

    def test_get_genre(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/genre/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_language(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/language/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_book(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/book/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_book_instance(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/book-instance/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_author(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/author/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_genres(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/genres/')
        self.assertEqual(response.status_code, 200)

    def test_get_languages(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/languages/')
        self.assertEqual(response.status_code, 200)

    def test_get_books(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_get_book_instances(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/book-instances/')
        self.assertEqual(response.status_code, 200)

    def test_get_authors(self):
        self.client.login(username="zaid", password="zaid")
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)
