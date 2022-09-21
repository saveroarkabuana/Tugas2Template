from urllib import response
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class mywatchlist(TestCase): 
    def test_contoh_app_url_exists(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlisthtml_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlistjson_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlistxml_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_contoh_app_using_to_do_list_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, "mywatchlist.html")


        