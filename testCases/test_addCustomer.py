import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomersMenu()
        self.addCustomer.clickOnCustomersMenuItem()

        self.addCustomer.clickOnAddNew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addCustomer.setEmail(self.email)
        self.addCustomer.setPassword("test123")
        self.addCustomer.setFirstName("Pavan")
        self.addCustomer.setLastName("Kumar")
        self.addCustomer.setGender("Male")
        self.addCustomer.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addCustomer.setCompanyName("busyQA")
        self.addCustomer.setCustomerRoles("Guests")
        self.addCustomer.setManagerOfVendor("Vendor 2")
        self.addCustomer.setAdminContent("This is for testing.........")
        self.addCustomer.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
