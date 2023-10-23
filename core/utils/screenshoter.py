import os
import time 
import sys
import traceback
import asyncio

sys.path.append("/core/utils/")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

USER_AGENT = os.getenv("USER_AGENT")

SPIDEY_DOMAIN = "spidey.fis-security.fpt.com"
SPIDEY_URL = f"https://{SPIDEY_DOMAIN}/dfir-team/channels/alerts"

IMAGE_DIR = "/core/media/"

MIN12 = 5
MIN5 = 5*60
MIN10 = 10*60
MIN15 = 15*60

BROWSER_OPTIONS = webdriver.ChromeOptions()      
BROWSER_OPTIONS.add_argument('--headless')
BROWSER_OPTIONS.add_argument('ignore-certificate-errors')
BROWSER_OPTIONS.add_argument("--start-maximized")
BROWSER_OPTIONS.add_argument(f'user-agent={USER_AGENT}')
BROWSER_OPTIONS.add_argument("--window-size=1920,1080")
BROWSER_OPTIONS.add_argument('--allow-running-insecure-content')
BROWSER_OPTIONS.add_argument("--disable-extensions")
BROWSER_OPTIONS.add_argument("--proxy-server='direct://'")
BROWSER_OPTIONS.add_argument("--proxy-bypass-list=*")
BROWSER_OPTIONS.add_argument("--start-maximized")
BROWSER_OPTIONS.add_argument('--disable-gpu')
BROWSER_OPTIONS.add_argument('--disable-dev-shm-usage')
BROWSER_OPTIONS.add_argument('--no-sandbox')

class Screenshoter():
    """ 
    A class to take a screenshot of a webpage after logging in with provided username and password
    """
    def __init__(self, logger, username: str, password: str, url):

        self.logger = logger
        self.wait = 3
        self.driver = webdriver.Chrome(options=BROWSER_OPTIONS)
        
        self.username = username
        self.password = password
        self.url= url
        
    def take_photo(self):
        try: 
            self.driver.get(self.url) # Navigating to the given URL.
            self.driver.save_screenshot(f"{IMAGE_DIR}export.png")
            
            self.logger.log_message(self.username, 'info')
            self.logger.log_message(self.password, 'info')
            self.logger.log_message("Taking screenshots in progress...", 'info')
            
            # Get user input -> enter username
            # element_name = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID,"loginId")))
            element_name = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.NAME,"username")))
            element_name.send_keys(self.username)
            
            # Get password input -> enter password
            # element_pass = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID,"loginPassword")))
            element_pass = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.NAME,"password")))
            element_pass.send_keys(self.password)
            
            # Click login button 
            # element_login = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID,"loginButton")))
            element_login = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
            element_login.click()
            
            self.driver.save_screenshot(f"{IMAGE_DIR}export.png")
            self.logger.log_message(f"Saved: {IMAGE_DIR}export.png", 'info')
            
            time.sleep(1)
     
        except Exception as error:
            traceback.print_exc()
            self.logger.log_message(error, "error")
        
if __name__ == "__main__":  
    
    pass 