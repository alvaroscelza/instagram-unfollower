import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Retrieve Instagram credentials from environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

if not username or not password:
    raise ValueError("Please set the INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD environment variables")

# Set up the Edge WebDriver with options
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)

# Navigate to Instagram login page
browser.get('https://www.instagram.com/')

# Wait for the login fields to be present
wait = WebDriverWait(browser, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

# Enter your login credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the login button
login_button = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
login_button.click()

# Optionally, wait for the home page to load
wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Home"]')))

# You can now perform other automated tasks on Instagram
