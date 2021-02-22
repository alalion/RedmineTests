import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login_valid(self):
        driver = self.driver
        driver.get(utils.URL)

        homepage = HomePage(driver)
        homepage.click_login_link()

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_logout_link()
            x = driver.title
            assert x == 'Redmine demo'

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime('%H-%M-%S_%m-%d-%Y')
            test_name = utils.whoami()
            screenshot_name = test_name + '_' + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver = self.driver
            driver.get_screenshot_as_file('/Users/alionap/PycharmProjects/AutomationFramework_1/screenshots/' +
                                          screenshot_name + '.png')
            raise
        except:
            print('There was an exception')
            curr_time = moment.now().strftime('%H-%M-%S_%m-%d-%Y')
            test_name = utils.whoami()
            screenshot_name = test_name + '_' + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver = self.driver
            driver.get_screenshot_as_file('/Users/alionap/PycharmProjects/AutomationFramework_1/screenshots/' +
                                          screenshot_name + '.png')
            raise

        else:
            print('No exceptions occurred')

        finally:
            print('I am inside finally block')


