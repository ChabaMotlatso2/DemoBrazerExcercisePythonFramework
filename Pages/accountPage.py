import time

import allure
from allure_commons.types import AttachmentType
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

    buttonTransactions_xpath = (By.XPATH, "//button[contains(.,'Transactions')]")


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
            return int(wait.until(EC.presence_of_element_located(self.textBalanceBeforeDeposit_xpath)).text)


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


    def getBalanceAfterTheDeposit(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for balanceAfterDeposit_element
        if check_element_presence(self.driver, self.textBalanceAfterDeposit_xpath):
            return int(wait.until(EC.presence_of_element_located(self.textBalanceAfterDeposit_xpath)).text)


    def verifyIfDepositWasSuccessful(self, balanceAfterDepositValue, balanceBeforeDepositValue, amountToDepositValue ):
        wait = WebDriverWait(self.driver, 1)
        if check_element_presence(self.driver, self.textSuccessfulDepositedMessage_xpath):
            if (wait.until(
                    EC.presence_of_element_located(self.textSuccessfulDepositedMessage_xpath)).text == 'Deposit Successful'
                    and balanceAfterDepositValue == balanceBeforeDepositValue + amountToDepositValue):
                print("Deposit was Successful.")
            else:
                print("Deposit failed.")


    def clickLogoutButton(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for logout_element
        if check_element_presence(self.driver, self.buttonLogout_xpath):
            # Click deposit Submit btn
            wait.until(EC.presence_of_element_located(self.buttonLogout_xpath)).click()


    def selectAllAccount(self, amountToDeposit):
        wait = WebDriverWait(self.driver, 1)
        # Check for customerLogin_element
        if check_element_presence(self.driver, self.selectAccount_xpath):
            # Create a Select object
            select_element = Select(wait.until(EC.presence_of_element_located(self.selectAccount_xpath)))

            # Loop through all options within the select element
            for option in select_element.options:
                time.sleep(1)

                option.click()

                time.sleep(2)  # Add a delay

                balanceBeforeDepositValue = self.getBalanceBeforeTheDeposit()
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=f'Balance for account "{option.text}" before deposit.',
                              attachment_type=AttachmentType.PNG)
                self.clickDepositTabButton()
                self.enterAmountToDeposit(amountToDeposit)
                self.clickDepositSubmitButtion()
                balanceAfterDepositValue = self.getBalanceAfterTheDeposit()
                self.verifyIfDepositWasSuccessful(balanceBeforeDepositValue, balanceAfterDepositValue, amountToDeposit)
                allure.attach(self.driver.get_screenshot_as_png(), name=f'Verify If Deposit for account "{option.text}" for Was Successful.',
                              attachment_type=AttachmentType.PNG)

    def clickTransactionsTabButton(self):
        wait = WebDriverWait(self.driver, 1)
        # Check for transactions_element
        if check_element_presence(self.driver, self.buttonTransactions_xpath):
            # Click Transactions btn
            wait.until(EC.presence_of_element_located(self.buttonTransactions_xpath)).click()