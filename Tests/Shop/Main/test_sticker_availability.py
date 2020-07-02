from Tests.browser_settings import init_browser
from Pages.Shop.MainPage import MainPage
from Tests.Helpers.UiHelper import UiHelper

browser = init_browser


# Проверяет наличие стикеров у товаров на главной странице
def test_check_stickers(browser) -> None:
    main_page = MainPage(browser)
    helper = UiHelper(browser)

    browser.get(main_page.URL)
    helper.wait_till_page_load(main_page.LOGOTYPE_CONTAINER)
    main_page.get_all_stickers_from_product_images()

    main_page.assert_stickers()
