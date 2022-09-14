from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem

# Create your tests here.
class Coba(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "Shampoo Kuda",
            item_price = 40000,
            item_stock = 3,
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

    
    def test_if_item_exists(self):
        coba1 = CatalogItem.objects.get(item_name = "Shampoo Kuda")
        coba2 = CatalogItem.objects.get(item_name = "PS5")
        self.assertIn("Shampoo Kuda", coba1.item_name)
        self.assertIn("PS5", coba2.item_name)