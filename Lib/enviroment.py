from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 브라우저 꺼짐 방지 test
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)