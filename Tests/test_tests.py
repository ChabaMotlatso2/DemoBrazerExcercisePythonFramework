import allure
import pytest

from Pages.customerPage import CustomerPage
from Pages.loginPage import LoginPage
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

        self.login.clickCustomerLoginButton()
        self.customerLogin.selectUserLogin()
        self.customerLogin.clickLoginButton()

        # initialize amounts
        balanceBeforeDepositValue = 0
        balanceAfterDepositValue = 0






