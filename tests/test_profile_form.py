import pytest
from pages.profile_form_page import ProfileFormPage
from utils.data_loader import load_user_data


@pytest.mark.parametrize("user", load_user_data())
def test_profile_form_submission(driver, config, user):
    page = ProfileFormPage(driver)
    driver.get(config['form_url'])

    page.fill_basic_info(user["firstname"], user["lastname"], user["email"], user["gender"],user["mobile"])
    page.fill_address(user["address"])
    page.select_state_city(user["state"], user["city"])
    page.submit_form()

    assert "Thanks for submitting the form" in page.get_success_message()