from django.test import TestCase
# Create your tests here.
from katalog.models import CatalogItem

class Test(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "Shampoo Kuda",
            item_price = 155295,
            item_stock = 5,
            description = "Cepet Tumbuh",
            rating = 10,
            item_url = "https://www.tokopedia.com/orvinhb/mane-n-tail-shampoo-355-ml-mane-n-tail-shampoo-kuda-sampo-kuda?extParam=ivf%3Dfalse%26whid%3D13393692&src=topads")
        
        CatalogItem.objects.create(
            item_name = "PS5",
            item_price = 10690000,
            item_stock = 1,
            description = "Newest Console on the Block",
            rating = 10,
            item_url = "https://www.tokopedia.com/nichosgamezone/ps5-playstation-5-disc-sony-indo?extParam=ivf%3Dfalse%26src%3Dsearch")

    def testing(self):
        testing1 = CatalogItem.objects.get(item_name = "Shampoo Kuda")
        testing2 = CatalogItem.objects.get(item_name = "PS5")
        self.assertIn("Shampoo Kuda", testing1.item_name)
        self.assertIn("PS5", testing2.item_name)
