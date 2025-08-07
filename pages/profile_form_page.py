from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfileFormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_basic_info(self, firstname,lastname, email, gender, mobile):
        self.driver.find_element(By.ID, "firstName").send_keys(firstname)
        self.driver.find_element(By.ID, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//input[@id = 'userEmail']").send_keys(email)
        gender_element = self.driver.find_element(By.XPATH, f"//label[normalize-space()='{gender}']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//label[normalize-space()='{gender}']"))
        )
        gender_element.click()
        self.driver.find_element(By.ID, "userNumber").send_keys(mobile)



    def fill_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)

    def select_state_city(self, state, city):
        state_field = self.driver.find_element(By.ID, "react-select-3-input")
        state_field.send_keys(state)
        state_field.send_keys(Keys.ENTER)

        city_field = self.driver.find_element(By.ID, "react-select-4-input")
        city_field.send_keys(city)
        city_field.send_keys(Keys.ENTER)

    def submit_form(self):
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "submit")))
        submit_btn.click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        ).text
