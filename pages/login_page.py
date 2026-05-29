from playwright.sync_api import expect

from pages.base_page import BasePage
from config.base import URL_BASE, E_MSG_LOGIN
import re



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.error = self.page.locator(".error-message-container")
        self.field_username = self.page.locator("#user-name")
        self.field_password = self.page.locator("#password")
        self.btn_login = self.page.get_by_role("button", name="Login")

    def fill_username(self, username):
        self.field_username.fill(username)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_btn_login(self):
        self.btn_login.click()

    def check_field_username(self, username):
        expect(self.field_username).to_have_value(username)

    def check_field_password(self, password):
        expect(self.field_password).to_have_value(password)

    def verify_login_success(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory.html"))

    def authorize(self, username, password):
        self.fill_username(username)
        self.check_field_username(username)
        self.fill_password(password)
        self.check_field_password(password)
        self.click_btn_login()

    def verify_page_loaded(self):
        expect(self.page).to_have_url(URL_BASE)

    def check_error_with_msg(self, error_msg=E_MSG_LOGIN):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(error_msg)
        return True

    def  login_procedure(self, user_, pass_):
         self.fill_username(user_)
         self.fill_password(pass_)
         self.click_btn_login()

