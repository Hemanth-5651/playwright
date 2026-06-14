class LoginPage:

    MOBILE_TEXTBOX = "input.xkp9Hl.ZvCKfk"

    def __init__(self, page):
        self.page = page

    def open_flipkart(self):
        self.page.goto("https://www.flipkart.com")

    def enter_mobile_number(self, mobile):
        self.page.locator(self.MOBILE_TEXTBOX).fill(mobile)