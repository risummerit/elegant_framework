from pytest import mark


@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://www.artofmanliness.com/skills/manly-know-how/how-a-cars-engine-works/')
    assert True
