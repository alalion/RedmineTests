class Locators:
    # login page objects
    username_textbox_id = 'username'
    password_textbox_id = 'password'
    autologin_checkbox_id = 'autologin'
    login_button_xpath = '//*[@id="login-form"]/form/table/tbody/tr[4]/td[2]/input'

    # home page objects
    login_link_class_name = 'login'
    logout_link_class_name = 'logout'
    myaccount_link_xpath = '//*[@id="account"]/ul/li[1]/a'
    projects_link_class_name = 'projects'

    # projects page objects
    add_new_project_link_xpath = '//*[@id="content"]/div[1]/a[1]'

    # add new project page object
    project_name_textbox_id = 'project_name'
    strong_text_format_button_class_name = 'jstb_strong'
    ordered_list_text_format_button_class_name = 'jstSpacer'
    project_description_textbox_id = 'project_description'
    project_identifier_textbox_id = 'project_identifier'
    project_homepage_textbox_id = 'project_homepage'
    project_is_public_checkbox_id = 'project_is_public'
    project_inherit_members_checkbox_id = 'project_inherit_members'
    issue_tracking_module_checkbox_value = 'issue_tracking'
    time_tracking_module_checkbox_value = 'time_tracking'
    news_module_checkbox_value = 'news'
    documents_module_checkbox_value = 'documents'
    files_module_checkbox_value = 'files'
    wiki_module_checkbox_value = 'wiki'
    forums_module_checkbox_value = 'boards'
    calendar_module_checkbox_value = 'calendar'
    gantt_module_checkbox_value = 'gantt'
    bug_trackers_checkbox_xpath = '//*[@id="project_trackers"]/label[1]/input'
    feature_trackers_checkbox_xpath = '//*[@id="project_trackers"]/label[2]/input'
    support_trackers_checkbox_xpath = '//*[@id="project_trackers"]/label[3]/input'
    create_button_xpath = '//*[@id="new_project"]/input[3]'
    create_and_continue_button_xpath = '//*[@id="new_project"]/input[4]'

    # my account page objects
    user_firstname_textbox_id = 'user_firstname'
    user_lastname_textbox_id = 'user_lastname'
    user_mail_textbox_id = 'user_mail'
    user_language_dropdown_id = 'user_language'
    user_ircnick_textbox_id = 'user_custom_field_values_3'
    user_mail_notification_dropdown_id = 'user_mail_notification'
    pref_no_self_notified_checkbox_id = 'pref_no_self_notified'
    pref_hide_mail_checkbox_id = 'pref_hide_mail'
    pref_time_zone_dropdown_id = 'pref_time_zone'
    pref_comments_sorting_dropdown_id = 'pref_comments_sorting'
    pref_warn_on_leaving_unsaved_checkbox_id = 'pref_warn_on_leaving_unsaved'
    delete_account_link_class_name = 'icon icon-del'
    change_password_link_xpath = '//*[@id="content"]/div[1]/a'

    # change password page objects
    current_password_textbox_name = 'password'
    new_password_textbox_name = 'new_password'
    new_password_confirmation_textbox_name = 'new_password_confirmation'
    apply_button_name = 'commit'
