from datetime import datetime, timedelta

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.accountPage import AccountPage
from Pages.customerPage import CustomerPage
from Pages.loginPage import LoginPage
from Pages.transactionListPage import TransactionListPage
from Utils.readProperties import ReadConfigs


class Tests:
    demoBrazerURL = ReadConfigs().getDemoBrazerURL()

    @pytest.mark.test1
    @allure.severity(allure.severity_level.MINOR)
    def test_1(self, setup):
        self.driver = setup
        self.driver.get(self.demoBrazerURL)
        self.driver.maximize_window()

        self.login = LoginPage(self.driver)
        self.customerLogin = CustomerPage(self.driver)
        self.account = AccountPage(self.driver)

        self.login.clickCustomerLoginButton()
        self.customerLogin.selectUserLogin()
        self.customerLogin.clickLoginButton()

        # initialize amount to deposit
        amountToDeposit = 1500

        self.account.selectFirstAccount()
        balanceBeforeDepositValue = self.account.getBalanceBeforeTheDeposit()
        allure.attach(self.driver.get_screenshot_as_png(), name="Balance for Test 1 before deposit", attachment_type=AttachmentType.PNG)
        self.account.clickDepositTabButton()
        self.account.enterAmountToDeposit(amountToDeposit)
        self.account.clickDepositSubmitButtion()
        balanceAfterDepositValue = self.account.getBalanceAfterTheDeposit()
        self.account.verifyIfDepositWasSuccessful(balanceBeforeDepositValue, balanceAfterDepositValue, amountToDeposit)
        allure.attach(self.driver.get_screenshot_as_png(), name="Verify If Deposit for Test 1 Was Successful", attachment_type=AttachmentType.PNG)
        self.account.clickLogoutButton()


    @pytest.mark.test2
    @allure.severity(allure.severity_level.MINOR)
    def test_2(self, setup):
        self.driver = setup
        self.driver.get(self.demoBrazerURL)
        self.driver.maximize_window()

        self.login = LoginPage(self.driver)
        self.customerLogin = CustomerPage(self.driver)
        self.account = AccountPage(self.driver)

        self.login.clickCustomerLoginButton()
        self.customerLogin.selectUserLogin()
        self.customerLogin.clickLoginButton()

        # initialize amount to deposit
        amountToDeposit = 1500

        self.account.selectAllAccount(amountToDeposit)

        self.account.clickLogoutButton()



    @pytest.mark.test3
    @allure.severity(allure.severity_level.MINOR)
    def test_3(self, setup):
        self.driver = setup
        self.driver.get(self.demoBrazerURL)
        self.driver.maximize_window()

        self.login = LoginPage(self.driver)
        self.customerLogin = CustomerPage(self.driver)
        self.account = AccountPage(self.driver)
        self.transactions = TransactionListPage(self.driver)

        self.login.clickCustomerLoginButton()
        self.customerLogin.selectUserLogin()
        self.customerLogin.clickLoginButton()

        # initialize amount to deposit
        amountToDeposit = 31459

        self.account.selectFirstAccount()
        balanceBeforeDepositValue = self.account.getBalanceBeforeTheDeposit()
        allure.attach(self.driver.get_screenshot_as_png(), name="Balance for Test 3 before deposit", attachment_type=AttachmentType.PNG)
        self.account.clickDepositTabButton()
        self.account.enterAmountToDeposit(amountToDeposit)
        self.account.clickDepositSubmitButtion()
        balanceAfterDepositValue = self.account.getBalanceAfterTheDeposit()
        self.account.verifyIfDepositWasSuccessful(balanceBeforeDepositValue, balanceAfterDepositValue, amountToDeposit)
        self.account.clickTransactionsTabButton()

        # Get the current date
        current_date = datetime.now()
        start_datetime = current_date.strftime('%Y-%m-%d')

        self.transactions.sendStartDate(start_datetime)

        self.transactions.verifyTransactionIsInTheList(amountToDeposit)

        self.account.clickLogoutButton()







