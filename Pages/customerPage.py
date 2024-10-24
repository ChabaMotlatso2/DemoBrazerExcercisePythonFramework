from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.checkElementPresence import check_element_presence
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CustomerPage:
    button_customerLogin_xpath = (By.XPATH, "//button[contains(.,'Customer Login')]")

    selectUser_xpath  = (By.XPATH, "//select[@id='userSelect']")
    button_login_xpath  = (By.XPATH, "//button[contains(.,'Login')]")

    def __init__(self, driver):
        self.driver = driver

    def selectUserLogin(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for customerLogin_element
        if check_element_presence(self.driver, self.selectUser_xpath):
            # Create a Select object
            select = Select(wait.until(EC.presence_of_element_located(self.selectUser_xpath)))

            # Select an option by visible text
            select.select_by_visible_text("Hermoine Granger")


    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for customerLogin_element
        if check_element_presence(self.driver, self.button_login_xpath):
            # Click on the Customer Login
            loginElement = wait.until(EC.visibility_of_element_located(self.button_login_xpath))
            loginElement.click()

