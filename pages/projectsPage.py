from locators.locators import Locators


class projectsPage:
    def __init__(self, driver):
        self.driver = driver

        self.projects_link_class_name = Locators.projects_link_class_name
        self.add_new_project_link_class_name = Locators.add_new_project_link_class_name