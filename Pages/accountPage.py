from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.checkElementPresence import check_element_presence
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AccountPage:

    selectAccount_xpath = (By.XPATH, "//select[@id='accountSelect']")

    textBalanceBeforeDeposit_xpath = (By.XPATH, "(//strong[@class='ng-binding'])[2]")

    buttonDeposit_xpath = (By.XPATH, "//button[contains(.,'Deposit')]")

    inputAmount_xpath = (By.XPATH, "//input[contains(@ng-model,'amount')]")

    buttonDeposit_submit_xpath = (By.XPATH, "//button[contains(@type,'submit')]")

    textBalanceAfterDeposit_xpath = (By.XPATH, "(//strong[@class='ng-binding'])[2]")

    textSuccessfulDepositedMessage_xpath = (By.XPATH, "//span[contains(@ng-show,'message')]")

    buttonLogout_xpath = (By.XPATH, "//button[contains(.,'Logout')]")

    #initialize amounts
    balanceBeforeDepositValue = 0
    balanceAfterDepositValue = 0

    Test1_AmountToDepositValue = 1500
    Test2_AmountToDepositValue = 1500
    Test3_AmountToDepositValue = 31459

    def __init__(self, driver):
        self.driver = driver

    def selectFirstAccount(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for customerLogin_element
        if check_element_presence(self.driver, self.selectAccount_xpath):
            # Create a Select object
            select = Select(wait.until(EC.presence_of_element_located(self.selectAccount_xpath)))

            # Select the first option (index 0)
            select.select_by_index(0)




