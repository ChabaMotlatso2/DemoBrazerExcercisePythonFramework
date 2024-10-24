from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.checkElementPresence import check_element_presence
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    button_customerLogin_xpath = (By.XPATH, "//button[contains(.,'Customer Login')]")

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLoginButton(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for customerLogin_element
        if check_element_presence(self.driver, self.button_customerLogin_xpath):
            # Click on the Customer Login
            loginCustomerElement = wait.until(EC.visibility_of_element_located(self.button_customerLogin_xpath))
            loginCustomerElement.click()
