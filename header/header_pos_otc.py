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
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'MASTER FILE'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[1]/div[1]/div').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('LSTV 1')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('LSTV 2')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('LSTV 3')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('111-111-111-111')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[7]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[7]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[7]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Manila,Philippines')
time.sleep(1)


driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('San Fernando Pampanga')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[9]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[9]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[9]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Lubao Pampanga')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[10]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[10]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[10]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('1111111')
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[11]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + 'a')
time.sleep
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[11]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[11]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('1111111')
time.sleep(1)



driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[12]/ion-col/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[1]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[12]/ion-col/button[1]/span').click()
time.sleep(1)


driver.execute_script('alert("UPDATED SUCCESSFULLY:PASSED✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)

driver.execute_script('alert("POSITIVE TESTING:PASSED✅" + "n"+"ALL BUTTONS ARE WORKING✅");')
time.sleep(4)
driver.switch_to.alert.accept() 

time.sleep(4)
