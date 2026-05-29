from playwright.sync_api import expect

from config.products import BACKPACK
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.btn_remove_card = self.page.locator("button:has-text('Remove')")
        self.sort_dropdown = self.page.locator(".product_sort_container")
        self.title = self.page.locator(".title")
        self.backpack1 = self.page.get_by_text(BACKPACK)
        self.price = self.page.locator(f"//*[text()='{BACKPACK}']/../../..//*[@class='inventory_item_price']")
        self.btn_add_to_card = self.page.locator(f"//*[text()='{BACKPACK}']/../../..//button")
        self.loc_price = "../../*[@class='inventory_item_price']"
        self.inventory_item_name = self.page.locator(".inventory_item_name")
        self.inventory_item_price = self.page.locator(".inventory_item_price")
        self.inventory_item_img = self.page.locator(".inventory_item_img img")
        self.shopping_cart_badge = self.page.locator(".shopping_cart_badge")
        self.inventory_item = self.page.locator(".inventory_item")


    def check_backpack1_visible(self):
        expect(self.backpack1).to_be_visible()

    def get_backpack1_price(self) -> str:
        price_ = self.price.text_content()
        return price_

    def check_is_price(self):
        assert self.get_backpack1_price().startswith("$")

    def click_btn_add_to_cart(self):
        self.btn_add_to_card.click()

    def check_have_title(self, title_text: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title_text)
        return True

    def get_product_cards_count(self) -> int:
        return self.inventory_item.count()

    def get_all_product_names(self) -> list[str]:
        return self.inventory_item_name.all_inner_texts()

    def get_all_product_prices(self) -> list[str]:
        return self.inventory_item_price.all_inner_texts()

    def are_all_images_valid(self) -> bool:
        images = self.inventory_item_img.all()

        for img in images:
            if img.evaluate("el => el.naturalWidth") == 0:
                return False

        return True

    def select_sort(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_all_product_prices_as_floats(self) -> list[float]:
        return [float(price.replace("$", "")) for price in
                self.get_all_product_prices()]

    def click_first_product_image(self):
        self.inventory_item_img.first.click()

    def get_cart_badge_count(self) -> int:
        if self.shopping_cart_badge.is_visible():
            return int(self.shopping_cart_badge.text_content())
        return 0

    def click_btn_remove_from_cart(self):
        self.btn_remove_card.click()


