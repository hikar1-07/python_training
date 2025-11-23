from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()
        # wd.find_element_by_xpath("//a[text()='home']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # self.return_to_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # wd.switch_to.alert.accept().click()
        self.return_to_contact_page()
        self.contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        Select = self.app.Select
        self.open_add_new_contact_page()
        self.fill_contact_form_name_data(contact)
        self.fill_contact_form_personal_data(contact)
        self.fill_contact_form_bdata(Select, contact)
        self.fill_contact_form_adata(Select, contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_first_contact_all(self, new_contact_data):
        wd = self.app.wd
        Select = self.app.Select
        self.contact_modify_presteps()
        self.fill_contact_form_name_data(new_contact_data)
        self.fill_contact_form_personal_data(new_contact_data)
        self.fill_contact_form_bdata(Select, new_contact_data)
        self.fill_contact_form_adata(Select, new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_first_contact_phone(self):
        wd = self.app.wd
        self.contact_modify_presteps()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_xpath("//input[@name='mobile']").clear()
        wd.find_element_by_xpath("//input[@name='mobile']").send_keys("73888000333")
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_first_contact_lastname(self):
        wd = self.app.wd
        self.contact_modify_presteps()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys("Zukova-Testovskaya")
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def contact_modify_presteps(self):
        wd = self.app.wd
        self.return_to_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def fill_contact_form_name_data(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)


    def fill_contact_form_personal_data(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home)
        self.change_contact_field_value("mobile", contact.mobile)
        self.change_contact_field_value("work", contact.work)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("email2", contact.email2)
        self.change_contact_field_value("email3", contact.email3)
        self.change_contact_field_value("homepage", contact.homepage)


    def fill_contact_form_adata(self, Select, contact):
        wd = self.app.wd
        if contact.aday is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        if contact.ayear is not None:
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def fill_contact_form_bdata(self, Select, contact):
        wd = self.app.wd
        if contact.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear is not None:
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)

    def change_contact_field_value(self, contact_field_name, contact_text):
        wd = self.app.wd
        if contact_text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(contact_text)

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_contact_page()
        self.contact_cache = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            lastname = cells[1].text
            firstname = cells[2].text
            self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
