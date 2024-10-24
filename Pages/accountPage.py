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

    def getBalanceBeforeTheDeposit(self):
        wait = WebDriverWait(self.driver, 1)
        if check_element_presence(self.driver, self.textBalanceBeforeDeposit_xpath):
            balanceBeforeDepositValue = int(wait.until(EC.presence_of_element_located(self.textBalanceBeforeDeposit_xpath)).text)


    def clickDepositTabButton(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for deposit_element
        if check_element_presence(self.driver, self.buttonDeposit_xpath):
            # Click deposit tab btn
            wait.until(EC.presence_of_element_located(self.buttonDeposit_xpath)).click()


    def enterAmountToDeposit(self, amountToDepositValue):
        wait = WebDriverWait(self.driver, 1)
        # Check for amount_element
        if check_element_presence(self.driver, self.inputAmount_xpath):
            # Enter amount
            wait.until(EC.presence_of_element_located(self.inputAmount_xpath)).send_keys(str(amountToDepositValue))

    def clickDepositSubmitButtion(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for deposit_submit_element
        if check_element_presence(self.driver, self.buttonDeposit_submit_xpath):
            # Click deposit Submit btn
            wait.until(EC.presence_of_element_located(self.buttonDeposit_submit_xpath)).click()