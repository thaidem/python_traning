from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("content").click()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_group_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_id("content").click()
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_group_page()

    def return_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.driver.quit()
