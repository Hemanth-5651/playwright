from pages.login_page import LoginPage

def test_enter_mobile_number(page):

    login_page = LoginPage(page)

    login_page.open_flipkart()

    page.wait_for_timeout(3000)

    login_page.enter_mobile_number("9876543210")

    page.wait_for_timeout(5000)