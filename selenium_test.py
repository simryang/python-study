import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller  # 현재 windows 10 에서는 잘 돌아가지만 rasberry pi 4 에서는 오류 발생
import os
import time
import sys
from paramiko import SSHClient, AutoAddPolicy  # for ssh auto password


doSelenium = True
doIpScan = False
sn = None
tel_no = None
if doSelenium:
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
        EC.element_to_be_clickable(
            (By.XPATH, wobj_detail_button_in_https_security_alert)
        )
    )
    driver.find_element_by_id("details-button").click()
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, wobj_proceed_link_in_https_security_alert)
        )
    )
    driver.find_element_by_id("proceed-link").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, wobj_login_button)))
    # id
    driver.find_element_by_xpath(wobj_user_text_field).send_keys("user")
    # pw
    pw = "qwe123!@#"
    pw2 = "wiznet1206!"
    # driver.find_element_by_xpath(wobj_password_text).send_keys(pw)
    driver.find_element_by_xpath(wobj_password_text).send_keys(pw2)
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
                (
                    By.XPATH,
                    "/html/body/div/div/div/div/div[4]/div[2]/div[2]/nav/ul/a[3]/li",
                )
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
# addr = "pi@192.168.7.10"
# cmd = "cat /proc/cpuinfo | grep Serial | awk -F'[: ]' '{print $3}'"
# _, ret = subprocess.getstatusoutput(f'ssh {addr} "{cmd}"')
# print(f"ret={ret}")

target = None
if doIpScan:
    import os
    import platform

    from datetime import datetime

    net = input("Enter the Network Address: ")
    net1 = net.split(".")
    a = "."

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Enter the Starting Number: "))
    en1 = int(input("Enter the Last Number: "))
    en1 = en1 + 1
    oper = platform.system()

    if oper == "Windows":
        ping1 = "ping -n 1 "
    elif oper == "Linux":
        ping1 = "ping -c 1 "
    else:
        ping1 = "ping -c 1 "
    t1 = datetime.now()
    print("Scanning in Progress:")

    import collections

    scand = collections.deque()
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)
        print(f"resp={response.readlines()}")
        print(f"resp[2]={response[2]}")
        if "TTL" in response[2].readlines():
            scand.append()
    #    for line in response.readlines():
    #       if(line.count("TTL")):
    #          break
    #       if (line.count("TTL")):
    #          print (addr, "--> Live")
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

doSshUpdateResource = True


def Oldssh_need_pw_typing():
    target = "192.168.100.10"
    pw = "arhis"
    newpw = f"sshpass -p'{pw}'"
    if doSshUpdateResource:
        cmd = "cd /home/pi/wiznet/skp_arhis; echo b4 $(ls resource); if [ ! -d resource/model ]; then mkdir resource/model; mv resource/*.tflite resource/model/; echo a4 $(ls resource); fi;"
        ret, res = subprocess.getstatusoutput(
            f'ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no pi@{target} "{cmd}"'
        )
        print(f"ssh update model a4 resource={res}(ret={ret})")
    doGetSn = True
    if doGetSn:
        cmd = "grep Serial /proc/cpuinfo | awk -F'[: ]' '{print $3}'; sudo reboot"
        _, res = subprocess.getstatusoutput(
            f'ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no pi@{target} "{cmd}"'
        )
        print(f"sn={res}")
        sn = res

    time.sleep(1)
    print(sn, tel_no)


if doSshUpdateResource:
    target = "192.168.100.10"
    test_target = "192.168.56.1"
    user = "pi"
    test_user = "sr"
    pw = "arhis"
    test_pw = ""
    client = SSHClient()
    # LOAD HOST KEYS
    # client.load_host_keys('~/.ssh/known_hosts')
    # client.load_host_keys("C:/Users/brad/.ssh/known_hosts")
    # client.load_system_host_keys()

    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(target, username=user, password=pw)
    # client.connect("10.1.1.83", username="root")

    # Run a command (execute PHP interpreter)
    # client.exec_command('hostname')
    cmd1 = "cd /home/pi/wiznet/skp_arhis; echo b4 $(ls resource); if [ ! -d resource/model ]; then mkdir resource/model; mv resource/*.tflite resource/model/; echo a4 $(ls resource); fi;"
    cmd2 = "grep Serial /proc/cpuinfo | awk -F'[: ]' '{print $3}'"
    cmd3 = "sudo reboot"
    p1stdin, p1stdout, p1stderr = client.exec_command(cmd1)
    p2stdin, p2stdout, p2stderr = client.exec_command(cmd2)
    result1 = p1stdout.read().decode("utf-8")
    err1 = p1stderr.read().decode("utf8")
    ret1 = p1stdout.channel.recv_exit_status()
    p1stdin.close()
    p1stdout.close()
    p1stderr.close()
    result2 = p2stdout.read().decode("utf-8")
    err2 = p2stderr.read().decode("utf8")
    ret2 = p2stdout.channel.recv_exit_status()
    p2stdin.close()
    p2stdout.close()
    p2stderr.close()
    _, _, _ = client.exec_command(cmd3)

    # Optionally, send data via STDIN, and shutdown when done
    # p1stdin.write("Hello world")
    # p1stdin.channel.shutdown_write()

    # Print output of command. Will wait for command to finish.
    # print(f'STDOUT: {p1stdout.read().decode("utf8")}')
    # print(f'STDERR: {p1stderr.read().decode("utf8")}')

    # Get return code from command (0 is default for success)
    # print(f"Return code: {p1stdout.channel.recv_exit_status()}")

    # Because they are file objects, they need to be closed
    # p1stdin.close()
    # p1stdout.close()
    # p1stderr.close()

    # Close the client itself
    client.close()


if doSshUpdateResource:
    target = "222.98.173.207"
    user = "sr"
    pw = "fndltmddd"
    client = SSHClient()
    # LOAD HOST KEYS
    # client.load_host_keys('~/.ssh/known_hosts')
    # client.load_host_keys("C:/Users/brad/.ssh/known_hosts")
    # client.load_system_host_keys()

    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(target, username=user, password=pw)
    # client.connect("10.1.1.83", username="root")

    # Run a command (execute PHP interpreter)
    # client.exec_command('hostname')
    # cmd = "cat /proc/cpuinfo"
    cmd1 = f"echo {}"
    p1stdin, p1stdout, p1stderr = client.exec_command(cmd1)
    result1 = p1stdout.read().decode("utf-8")
    err1 = p1stderr.read().decode("utf8")
    ret1 = p1stdout.channel.recv_exit_status()
    p1stdin.close()
    p1stdout.close()
    p1stderr.close()
    _, _, _ = client.exec_command(cmd3)

    # Close the client itself
    client.close()


sys.exit(0)
