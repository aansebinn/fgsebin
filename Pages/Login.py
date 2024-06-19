import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Lib.enviroment import *


def login():
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