from Tests.browser_settings import init_browser
from Pages.Shop.MainPage import MainPage

browser = init_browser


def test_check_stickers(browser):
    main_page = MainPage(browser)

    browser.get(main_page.URL)
    main_page.get_all_product_images()

    main_page.assert_stickers()
