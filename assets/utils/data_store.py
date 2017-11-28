import re
from random import randint
from faker import Faker


class DataStore():
    """ If I could spent some more time on this I would drop hashes idea. But for now - 'whatever works'. """
    last_merchant = None
    last_product = None

    def generate_merchant(self):
        fake = Faker()
        merchant = {
            "store_name":       fake.company(),
            "store_email":      fake.safe_email(),
            "store_password":   fake.password(),
            "user_name":        fake.first_name(),
            "user_phone":       fake.msisdn(),
            "user_country":     self.fake_country()
        }
        merchant["store_normalized"] = self.normalize_store_name(merchant["store_name"])
        self.last_merchant = merchant
        print "Merchant: " + str(merchant)  # For debugging. Obviously this should be sent to logge stdout.
        return merchant

    def generate_product(self):
        fake = Faker()
        product = {
            "name":              fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            "description":       fake.text(max_nb_chars=200, ext_word_list=None),
            "image":             "/test_data/image1.jpg",
            "visibility":        False,
            "sku":               fake.ean(length=13),
            "price":             float(randint(10000.0, 100000.0))/100,
            "price_type":        randint(1, 2),
            "tax_type":          "other",
            "tax_amount":        randint(10, 30),
            "qty":               randint(0, 10000),
            "buy_if_empty":      True,
            "short_description": fake.text(max_nb_chars=400, ext_word_list=None),
            "weight":            randint(0, 10000),
            "width":             randint(0, 10000),
            "height":            randint(0, 10000),
            "depth":             randint(0, 10000),
            "diameter":          randint(0, 10000),
            "require_shipping":  False,  # False - so selenium will click other radio.
            "vendor":            None,
            "tag":               "TV",
            "seo_address":       fake.last_name(),
            "seo_title":         fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
            "seo_keywords":      "some, strange, keywords",
            "seo_description":   fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        }
        self.last_product = product
        print "Product: " + str(product)  # Debugging again.
        return product

    def normalize_store_name(self, phrase):
        """ Dashes instead of special chars and lowercase. I bet it is more sophisticated on your side. """
        return re.sub('[^0-9a-zA-Z.-]+', '-', phrase).lower()


    def fake_country(self):
        """
        Shoplo has polish localization - I don't want to complicate those tests so it will has both polish and english
        strings.
        """
        while True:
            code = Faker().country_code()
            if code != "pl":
                return code.lower()
