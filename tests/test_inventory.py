from config.base import URL_INVENTARY
from config.products import ExpectedProduct
from config.users import USER1_NAME, USER_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestInventory:

    def test_inv_001(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        cards_count = inventory_page.get_product_cards_count()

        assert cards_count == 6, f"Ожидалось 6 товаров, но найдено {cards_count}"

    def test_inv_002(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        expected_names = [product.value[0] for product in ExpectedProduct]

        inventory_page = InventoryPage(page)
        actual_names = inventory_page.get_all_product_names()

        assert actual_names == expected_names, f"Списки не совпадают!\nОжидалось: {expected_names}\nПолучено: {actual_names}"

    def test_inv_003(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        expected_prices = [product.value[1] for product in ExpectedProduct]

        inventory_page = InventoryPage(page)
        actual_prices = inventory_page.get_all_product_prices()

        assert actual_prices == expected_prices, f"Цены не совпадают!\nОжидалось: {expected_prices}\nПолучено: {actual_prices}"

    def test_inv_004(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        assert inventory_page.are_all_images_valid(), "Найдены битые изображения товаров!"


    def test_inv_005(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)

        inventory_page.select_sort("lohi")
        actual_prices = inventory_page.get_all_product_prices_as_floats()
        expected_prices = sorted(actual_prices)

        assert actual_prices ==  expected_prices
        f"Цены не отсортированы по возрастанию! Получено: {actual_prices}"


