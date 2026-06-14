def test_open_flipkart(page):
    page.goto("https://www.flipkart.com")

    # Wait for page to load
    page.wait_for_timeout(5000)

    print("Flipkart opened successfully")