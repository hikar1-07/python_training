class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_edit_page_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        # Select = self.app.Select
        self.open_edit_page_contact()
        # init contact creation
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        Select = self.app.Select
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # birthday form
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # anniversary form
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_contact_page()
        # init contact modify
        wd.find_element_by_name("selected[]").click()
        # submit modify
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # wd.switch_to.alert.accept().click()
        self.return_to_contact_page()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # wd.find_element_by_xpath("//a[text()='home']").click()

    def change_field_value(self, contact_field_name, contact_text):
        wd = self.app.wd
        if contact_text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(contact_text)