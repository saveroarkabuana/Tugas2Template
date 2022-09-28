from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class Testlistmywatchlist(TestCase): 
    def test_contoh_app_url_exists(self):
        response = Client().get('/todolist/')
        self.assertEqual(response.status_code,200)