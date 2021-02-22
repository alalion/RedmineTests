import pytest
import allure
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.projectsPage import ProjectsPage
from pages.newprojectPage import NewProjectPage
from utils import utils as utils
import moment


@pytest.mark.usefixtures("test_setup")
class TestAddingNewProject():

    def test_adding_project(self):
        try:

            driver = self.driver
            driver.get(utils.URL)

            homepage = HomePage(driver)
            homepage.click_login_link()

            login = LoginPage(driver)
            login.enter_username(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            login.click_login()

            homepage.click_projects_link()

            prjcts_page = ProjectsPage(driver)
            prjcts_page.click_new_project_link()

            new_prjct_page = NewProjectPage(driver)
            new_prjct_page.enter_project_name('New Test Project Pangoline')
            # new_prjct_page.enter_project_identifier('Test Identifier')
            driver.implicitly_wait(10)
            new_prjct_page.click_create_button()


            #assert actual_text == self.driver.find_element_by_id('flash_notice').get_attribute()
          #  self.driver.find_element_by_partial_link_text('Successful creation.')
           # print('Successful creation.')

        except:
            print('Project is NOT created')
            currTime = moment.now().strftime('%H-%M-%S_%m-%d-%Y')
            testName = utils.whoami()
            screenshotName = testName + '_' + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver = self.driver
            driver.get_screenshot_as_file('/Users/alionap/PycharmProjects/AutomationFramework_1/screenshots/' +
                                          screenshotName + '.png')
            raise
