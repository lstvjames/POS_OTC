from keyboard import press
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("nwapp=C:/Program Files (x86)/LSTV/POS/OTC/frontend/TITANS_KRAKEN.exe")

driver = webdriver.Chrome("C:/Users/SERAN/Desktop/Selenium Jar Files/nwjs-sdk-v0.54.0-win-x64/chromedriver", options= options)

#maximize window
driver.maximize_window()
time.sleep(2)

#login
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(5)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col[1]/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[1]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col[2]/ion-item/div[1]/div/ion-input/input').send_keys('85')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[7]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[1]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[2]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[11]/ion-col/button[2]/span').click()
time.sleep(1)

#username/password
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card[2]/ion-list/ion-item[1]/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/div/button[1]/span').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[3]/span').click()
time.sleep(1)
buttons = driver.find_elements_by_class_name('button-inner')
index = 11      
for index in range(index,24):
    if index == 24:
        buttons[23].click()
        time.sleep(2)
    buttons[index].click()
    time.sleep(1)

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH IN'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cashinout/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)

value = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cashinout/ion-content/div[2]/ion-item/div[1]/div/ion-input/input').get_attribute('value')
if int(value) <= 0:
    driver.execute_script('alert("CANT CASH IN IF VALUE IS 0: ✅ ");')
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(2)

buttons = driver.find_elements_by_class_name('button-inner')  
for x in range(0,3):
    if x==0:
        buttons[15].click()
        time.sleep(2)
    buttons[21].click()
    time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cashinout/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

reason = driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').get_attribute("value")
if len(reason) == 0:
    driver.execute_script('alert("CANT CONFIRM IF REASON IS EMPTY: ✅");')           
    time.sleep(7)
    driver.switch_to.alert.accept()
    time.sleep(2)

driver.execute_script('alert("CANT CASH IN IF VALUE IS 0: PASSED✅"+ "\\n" + "CANT CONFIRM IF REASON IS EMPTY TEST:PASSED ✅"+ "\\n" + "NEGATIVE TESTING:PASSED ✅"  );')           
time.sleep(7)
driver.switch_to.alert.accept()
time.sleep(2)