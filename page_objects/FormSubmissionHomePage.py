from selenium.webdriver.common.by import By



class SubmissionHomepage:

    def __init__(self, driver):
        self.driver= driver

    name_field = (By.XPATH, "//div[@class='form-group']/label[text()='Name']/following-sibling::input")

    password_field = (By.XPATH,"//input[@placeholder='Password']")

    submit_button = (By.ID, "exampleInputPassword1")

    home_page_url= ("https://rahulshettyacademy.com/angularpractice/")


    def enter_name(self, text):
        self.driver.find_element(*SubmissionHomepage.name_field).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(*SubmissionHomepage.password_field).send_keys(text)

    def click_on_submit_button(self):
        self.driver.find_element(*SubmissionHomepage.submit_button).click()

    def go_to_home_page(self):
        self.driver.get(SubmissionHomepage.home_page_url)

