from Tests.browser_settings import init_browser
from Pages.Shop.MainPage import MainPage

browser = init_browser


def test_open_campaign_product(browser):
    main_page = MainPage(browser)

    browser.get(main_page.URL)
    main_page.open_product_page(main_page.FIRST_CAMPAIGN_PRODUCT_HREF)
    main_page.product_page.get_product_name_and_prices()
    main_page.product_page.get_product_prices_styles()

    main_page.product_page.assert_product_name_and_price('Yellow Duck', '$20', '$18')
