import allure

from config.base import URL_INVENTARY
from config.products import ExpectedProduct
from config.users import USER1_NAME, USER_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.epic("Инвентарь")
@allure.feature("Страница товаров")
class TestInventory:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка общего количества карточек товаров")
    def test_inv_001(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        cards_count = inventory_page.get_product_cards_count()

        assert cards_count == 6, f"Ожидалось 6 товаров, но найдено {cards_count}"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка соответствия названий всех товаров")
    def test_inv_002(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        expected_names = [product.value[0] for product in ExpectedProduct]

        inventory_page = InventoryPage(page)
        actual_names = inventory_page.get_all_product_names()

        assert actual_names == expected_names, f"Списки не совпадают!\nОжидалось: {expected_names}\nПолучено: {actual_names}"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка соответствия цен всех товаров")
    def test_inv_003(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        expected_prices = [product.value[1] for product in ExpectedProduct]

        inventory_page = InventoryPage(page)
        actual_prices = inventory_page.get_all_product_prices()

        assert actual_prices == expected_prices, f"Цены не совпадают!\nОжидалось: {expected_prices}\nПолучено: {actual_prices}"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка валидности изображений товаров")
    def test_inv_004(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        assert inventory_page.are_all_images_valid(), "Найдены битые изображения товаров!"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортировка цен по возрастанию (low to high)")
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


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортировка цен по убыванию (high to low)")
    def test_inv_006(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        inventory_page.select_sort("hilo")

        actual_prices = inventory_page.get_all_product_prices_as_floats()
        assert actual_prices == sorted(actual_prices, reverse=True), f"Цены не отсортированы по убыванию! Получено: {actual_prices}"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортировка названий по алфавиту (A to Z)")
    def test_inv_007(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        inventory_page.select_sort("az")

        actual_names = inventory_page.get_all_product_names()
        assert actual_names == sorted(actual_names), f"Названия не отсортированы по алфавиту! Получено: {actual_names}"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сохранение состояния карточки после изменения сортировки")
    def test_inv_008(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        inventory_page.click_btn_add_to_cart()

        inventory_page.select_sort("hilo")
        inventory_page.check_backpack1_visible()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Переход на детальную страницу товара по клику на картинку")
    def test_inv_009(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        inventory_page.click_first_product_image()

        actual_url = page.url
        assert "inventory-item" in actual_url, f"Ожидался переход на детальную страницу товара, но текущий URL: {actual_url}"


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Добавление и последующее удаление товара из корзины")
    def test_inv_010(self, page):

        login_page = LoginPage(page)
        login_page.open()
        login_page.login_procedure(USER1_NAME, USER_PASSWORD)
        login_page.expect_to_have_url(URL_INVENTARY)

        inventory_page = InventoryPage(page)
        inventory_page.click_btn_add_to_cart()

        assert inventory_page.get_cart_badge_count() == 1, "Товар не добавился в корзину!"

        inventory_page.click_btn_remove_from_cart()

        assert inventory_page.get_cart_badge_count() == 0, "Товар не удалился из корзины после нажатия 'Remove'!"
