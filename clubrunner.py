from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Clubrunner:

    def __init__(self, site):
        self.url = f'https://admin.clubrunner.ca/{site}'
        self.browser = browser = webdriver.Chrome()

    def login(self):
        login_path = 'User/Login'

        login_url = f'{self.url}/{login_path}'

        # Navigate to the URL
        self.browser.get(login_url)

        # Wait for the logout link to be clickable
        try:
            logout_link = WebDriverWait(self.browser, 600).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))
            )
            print("Logout link found, carry on.")
        except TimeoutException:
            print("Timed out waiting for the logout link to appear.")

        return

    def send_meeting_reminder(self):

        self.login()

        self.browser.get(f'{self.url}/CommunicationEmail/Details?ShowMineOnly=True&EmailType=Communication')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Members > .custom-control > .far-icon"))).click()
        self.browser.find_element(By.ID, "Subject").click()
        self.browser.find_element(By.ID, "Subject").send_keys("Rotary Meeting Reminder")
        self.browser.find_element(By.ID, "cke_64").click()
        #...
        self.browser.find_element(By.CSS_SELECTOR, ".field-group:nth-child(2) .fas-icon").click()
        print("Please press Enter to continue...")
        input()  # Python will pause here until Enter is pressed
        print("Continuing script...")
        self.browser.quit()

# Do additional tasks or interactions here

# Close the browser when done



# push minutes to club runner

# create speaker event from spreasheet

# send meeting reminder


#