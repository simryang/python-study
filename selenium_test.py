from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller
import os
import time

t_begin = time.time()
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
chrome_name = "chromedriver.exe"
try:
    driver = webdriver.Chrome(os.path.join(chrome_ver, chrome_name))
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(os.path.join(chrome_ver, chrome_name))
# wait = driver.implicitly_wait(10)
# driver = webdriver.Chrome("chromedriver.exe")
wait = WebDriverWait(driver, 1000)
driver.get("https://192.168.1.1")

wobj_detail_button_in_https_security_alert = '//*[@id="details-button"]'
wobj_proceed_link_in_https_security_alert = '//*[@id="proceed-link"]'
wobj_login_button = "/html/body/div/div/div/div/div/div[2]/div/form/div/button"
wobj_user_text_field = "/html/body/div/div/div/div/div/div[2]/div/form/div/input[1]"
wobj_password_text = "/html/body/div/div/div/div/div/div[2]/div/form/div/input[2]"
wobj_HA_menu = '//*[@id="ui-accordion-1-header-2"]'
wobj_auto_link_sensing_menu = (
    '//*[@id="ui-accordion-1-panel-2"]/div/ul/li[2]/span/span[2]/a'
)
wobj_status_check_address = (
    '//*[@id="page-div"]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[2]'
)
wobj_network_menu = '//*[@id="ui-accordion-1-header-1"]'
wobj_unknown_ip = (
    '//*[@id="page-div"]/div/div/div/div[3]/div[2]/table/tbody/tr[3]/td[5]/label'
)
wobj_interface = '//*[@id="page-div"]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/form/table/tbody/tr[1]/td[2]/label'  # eth1
wobj_if_type = '//*[@id="page-div"]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/form/table/tbody/tr[2]/td[2]/label[2]'  # LTE (LTE+WCDMA)
wobj_decibel = '//*[@id="page-div"]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/form/table/tbody/tr[11]/td[2]/label[1]'  # -66
wobj_decibel_unit = '//*[@id="page-div"]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/form/table/tbody/tr[11]/td[2]/label[2]'  # dBm
wobj_tel_no = '//*[@id="page-div"]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/form/table/tbody/tr[16]/td[2]/label'  # 전번

wait.until(
    EC.element_to_be_clickable((By.XPATH, wobj_detail_button_in_https_security_alert))
)
driver.find_element_by_id("details-button").click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, wobj_proceed_link_in_https_security_alert))
)
driver.find_element_by_id("proceed-link").click()
wait.until(EC.element_to_be_clickable((By.XPATH, wobj_login_button)))
# id
driver.find_element_by_xpath(wobj_user_text_field).send_keys("user")
# pw
driver.find_element_by_xpath(wobj_password_text).send_keys("wiznet1206!")
# login button
driver.find_element_by_xpath(wobj_login_button).click()

# 경고창 없애기. 경고창이 없을 때는 timeout 으로 강제 종료됨... 대책 필요
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    # alert.accept()
    # time.sleep(10)
except Exception as e:
    print("no alert")

if False:
    # HA 메뉴
    wait.until(EC.element_to_be_clickable((By.XPATH, wobj_HA_menu)))
    driver.find_element_by_xpath(wobj_HA_menu).click()
    # 자동링크감지 링크
    wait.until(EC.element_to_be_clickable((By.XPATH, wobj_auto_link_sensing_menu)))
    driver.find_element_by_xpath(wobj_auto_link_sensing_menu).click()
    # 상태 확인 주소
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                wobj_status_check_address,
            )
        )
    )
    ip_public = driver.find_element_by_xpath(wobj_status_check_address).text
    print(f"public IP address = {ip_public}")
    # 네트워크 메뉴
    wait.until(EC.element_to_be_clickable((By.XPATH, wobj_network_menu)))
    driver.find_element_by_xpath(wobj_network_menu).click()
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                wobj_unknown_ip,
            )
        )
    )
    ip_public2 = driver.find_element_by_xpath(wobj_unknown_ip).text
    ip_str = ip_public2.split("/")[0]
    print(f"public IP address = {ip_str}")

    ""
    # 화면 상단 모니터 아이콘의 역삼각 드랍박스 아이콘
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div/div[4]/div[2]/div[2]/nav/ul/a[3]/li")
        )
    )
    driver.find_element_by_xpath('//*[@id="ui-accordion-1-header-1"]').click()
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div/div[4]/div[5]/ul/li[13]/a")
        )
    )
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div[4]/div[5]/ul/li[13]/a"
    ).click()
    # driver.find_element_by_id("ui-accordion-1-header-1").click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="details-button"]'))).click()

driver.get("https://192.168.1.1/#/monitor/lte")

wait.until(EC.element_to_be_clickable((By.XPATH, wobj_decibel)))
decibel = driver.find_element_by_xpath(wobj_decibel).text
print(f"decibel={decibel}")
wait.until(EC.element_to_be_clickable((By.XPATH, wobj_tel_no)))
tel_no = driver.find_element_by_xpath(wobj_tel_no).text
print(f"tel_no={tel_no}")
# time.sleep(100)
driver.close()
driver.quit()
print(f"Elapsed time = {time.time() - t_begin:.2f}")