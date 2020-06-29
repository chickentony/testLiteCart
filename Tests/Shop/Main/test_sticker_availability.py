from Tests.browser_settings import init_browser
from Pages.Shop.MainPage import MainPage
from Tests.Helpers.UiHelper import UiHelper

browser = init_browser


def test_check_stickers(browser):
    main_page = MainPage(browser)
    helper = UiHelper(browser)

    browser.get(main_page.URL)
    helper.wait_till_page_load('//div[@id="logotype-wrapper"]')
    main_page.get_all_product_images()

    main_page.assert_stickers()
