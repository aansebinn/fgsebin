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

# 로그인 페이지 불러오기 test
url = "https://dev-www.fashiongo.net/login?returnUrl=%2F"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

# 쿠키 팝업 닫기

driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()

# 아이디 비밀번호 입력 후 로그인

id = driver.find_element(By.CSS_SELECTOR,"#email-inp")
id.click()
id.send_keys("ansebin@yopmail.com")

password = driver.find_element(By.CSS_SELECTOR,"#pwd_inp")
password.click()
password.send_keys("Qwe123!")

driver.find_element(By.CSS_SELECTOR,"#btn-signin").click()

# 드라이버 종료
time.sleep(5)
driver.quit()