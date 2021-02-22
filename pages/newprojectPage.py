from locators.locators import Locators


class NewProjectPage:
    def __init__(self, driver):
        self.driver = driver

        self.add_new_project_link_xpath = Locators.add_new_project_link_xpath

    def enter_project_name(self, project_name):
        self.driver.find_element_by_id(Locators.project_name_textbox_id).clear()
        self.driver.find_element_by_id(Locators.project_name_textbox_id).send_keys(project_name)

    def click_strong_format_button(self):
        self.driver.find_element_by_class_name(Locators.strong_text_format_button_class_name).click()

    def click_ordered_list_button(self):
        self.driver.find_element_by_class_name(Locators.ordered_list_text_format_button_class_name).click()

    def enter_project_description(self, description):
        self.driver.find_element_by_id(Locators.project_description_textbox_id).send_keys(description)

    def enter_project_identifier(self, identifier):
        self.driver.find_element_by_id(Locators.project_identifier_textbox_id).send_keys(identifier)

    def enter_project_homepage(self, homepage):
        self.driver.find_element_by_id(Locators.project_homepage_textbox_id).send_keys(homepage)

    def click_issue_tracking_checkbox(self):
        self.driver.find_element_by_value(Locators.issue_tracking_module_checkbox_value).click()

    def click_time_tracking_checkbox(self):
        self.driver.find_element_by_value(Locators.time_tracking_module_checkbox_value).click()

    def click_news_checkbox(self):
        self.driver.find_element_by_value(Locators.news_module_checkbox_value).click()

    def click_documents_checkbox(self):
        self.driver.find_element_by_value(Locators.documents_module_checkbox_value).click()

    def click_files_checkbox(self):
        self.driver.find_element_by_value(Locators.files_module_checkbox_value).click()

    def click_wiki_checkbox(self):
        self.driver.find_element_by_value(Locators.wiki_module_checkbox_value).click()

    def click_forums_checkbox(self):
        self.driver.find_element_by_value(Locators.forums_module_checkbox_value).click()

    def click_calendar_checkbox(self):
        self.driver.find_element_by_value(Locators.calendar_module_checkbox_value).click()

    def click_gantt_checkbox(self):
        self.driver.find_element_by_value(Locators.gantt_module_checkbox_value).click()

    def click_bug_checkbox(self):
        self.driver.find_element_by_xpath(Locators.bug_trackers_checkbox_xpath).click()

    def click_feature_checkbox(self):
        self.driver.find_element_by_xpath(Locators.feature_trackers_checkbox_xpath).click()

    def click_support_checkbox(self):
        self.driver.find_element_by_xpath(Locators.support_trackers_checkbox_xpath).click()

    def click_create_button(self):
        self.driver.find_element_by_xpath(Locators.create_button_xpath).click()

    def click_create_and_continue_button(self):
        self.driver.find_element_by_xpath(Locators.create_and_continue_button_xpath).click()
