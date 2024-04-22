import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.add_customer = AddCustomer(self.driver)
        self.add_customer.clickOnCustomersMenu()
        self.add_customer.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        search_cust = SearchCustomer(self.driver)
        search_cust.setEmail("victoria_victoria@nopCommerce.com")
        search_cust.clickSearch()
        time.sleep(5)
        status = search_cust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
