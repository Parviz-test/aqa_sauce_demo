from enum import Enum


class ExpectedProduct(Enum):
    BACKPACK = ("Sauce Labs Backpack", "$29.99")
    BIKE_LIGHT = ("Sauce Labs Bike Light", "$9.99")
    BOLT_TSHIRT = ("Sauce Labs Bolt T-Shirt", "$15.99")
    FLEECE_JACKET = ("Sauce Labs Fleece Jacket", "$49.99")
    ONESIE = ("Sauce Labs Onesie", "$7.99")
    RED_TSHIRT = ("Test.allTheThings() T-Shirt (Red)", "$15.99")

    def init(self, title, price):
        self.title = title
        self.price = price

BACKPACK = "Sauce Labs Backpack"
TITLE_INVENTORY = "Products"