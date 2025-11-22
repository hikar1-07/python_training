class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # wd.find_element_by_xpath("//a[text()='home']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # wd.switch_to.alert.accept().click()
        self.return_to_contact_page()

    def create_contact(self, contact):
        wd = self.app.wd
        Select = self.app.Select
        self.open_add_new_contact_page()
        # fill contact firm
        self.contacts_name_data(contact)
        self.contacts_personal_data(contact)
        # birthday form
        self.contacts_bdata_form(Select, contact)
        # anniversary form
        self.contacts_adata_form(Select, contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_contact_page()

    def modify_first_contact_all(self, contact):
        wd = self.app.wd
        Select = self.app.Select
        self.contact_modify_presteps()
        # fill contact firm
        self.contacts_name_data(contact)
        self.contacts_personal_data(contact)
        # birthday form
        self.contacts_bdata_form(Select, contact)
        # anniversary form
        self.contacts_adata_form(Select, contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()

    def modify_first_contact_phone(self):
        wd = self.app.wd
        self.contact_modify_presteps()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_xpath("//input[@name='mobile']").clear()
        wd.find_element_by_xpath("//input[@name='mobile']").send_keys("72888000000")
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()

    def modify_first_contact_lastname(self):
        wd = self.app.wd
        self.contact_modify_presteps()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys("Testovskaya")
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.return_to_contact_page()

    def contact_modify_presteps(self):
        wd = self.app.wd
        self.return_to_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def contacts_name_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def contacts_personal_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def contacts_adata_form(self, Select, contact):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def contacts_bdata_form(self, Select, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)