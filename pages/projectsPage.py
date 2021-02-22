from locators.locators import Locators


class ProjectsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_project_link(self):
        self.driver.find_element_by_xpath(Locators.add_new_project_link_xpath).click()
