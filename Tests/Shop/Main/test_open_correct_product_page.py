from Tests.browser_settings import init_browser
from Pages.Shop.MainPage import MainPage
from Tests.Helpers.UiHelper import UiHelper

browser = init_browser


# Проверяет что открывается корректный первый товар в категории "акции"
def test_open_campaign_product(browser):
    main_page = MainPage(browser)
    helper = UiHelper(browser)

    browser.get(main_page.URL)
    helper.wait_till_page_load(main_page.LOGOTYPE_CONTAINER)
    main_page.get_product_prices_styles()
    main_page.open_product_page(main_page.FIRST_CAMPAIGN_PRODUCT_HREF)
    main_page.product_page.get_product_name_and_prices()
    main_page.product_page.get_product_prices_styles()

    assert main_page.product_regular_price_styles['color'] == 'rgba(119, 119, 119, 1)'
    assert main_page.product_regular_price_styles['text-decoration'] == 'line-through solid rgb(119, 119, 119)'
    assert main_page.product_regular_price_styles['font-size'] == '14.4px'
    assert main_page.product_sale_price_styles['color'] == 'rgba(204, 0, 0, 1)'
    assert main_page.product_sale_price_styles['text-decoration'] == 'none solid rgb(204, 0, 0)'
    assert main_page.product_sale_price_styles['font-size'] == '18px'
    assert main_page.product_page.product_regular_price_styles['color'] == 'rgba(102, 102, 102, 1)'
    assert main_page.product_page.product_regular_price_styles[
               'text-decoration'] == 'line-through solid rgb(102, 102, 102)'
    assert main_page.product_page.product_regular_price_styles['font-size'] == '16px'
    assert main_page.product_page.product_sale_price_styles['color'] == 'rgba(204, 0, 0, 1)'
    assert main_page.product_page.product_sale_price_styles['text-decoration'] == 'none solid rgb(204, 0, 0)'
    assert main_page.product_page.product_sale_price_styles['font-size'] == '22px'
    assert main_page.product_page.product_name == 'Yellow Duck'
    assert main_page.product_page.product_regular_price == '$20'
    assert main_page.product_page.sale_price == '$18'
