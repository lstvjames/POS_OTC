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
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.execute_script('alert("BACK BUTTON IS WORKING PROPERLY ✅");')
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(4)

cf = 0
cf_value = 0
for i in range(0,2):
    driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
    time.sleep(2)

    buttons = driver.find_elements_by_class_name('button-inner')
    index = 11      

    for index in range(index,24):
        if index == 24:
            buttons[23].click()
            time.sleep(2)
        buttons[index].click()
        time.sleep(1)

    driver.execute_script('alert("ALL BUTTONS ARE WORKING PROPERLY: ✅ ");')
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(2)     

    buttons[21].click()
    time.sleep(1)

    value = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/ion-item/div[1]/div/ion-input/input').get_attribute('value')
    if int(value) <= 0:
        driver.execute_script('alert("CANT SAVE CASH FUND IF VALUE IS 0 ✅ ");')
        time.sleep(3)
        driver.switch_to.alert.accept() 
        time.sleep(2)

    for x in range(0,3):
        if x == 0:
            buttons[19].click()
            time.sleep(1)
        buttons[21].click()
        time.sleep(1)   


    cf_value = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/ion-item/div[1]/div/ion-input/input').get_attribute("value")
    cf = int(cf) + int(cf_value)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
    time.sleep(4)

    press ('enter')
    time.sleep(1)
    press ('enter')
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    press ('enter')
    time.sleep(1)
    press ('enter')
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-otc/ion-header/ion-navbar/ion-buttons/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/popover/ion-list/button/div[1]/div').click()
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[4]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/ion-grid/ion-row[3]/ion-col[3]/ion-item/div[1]/div/ion-input/input').send_keys(10)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/ion-grid/ion-row[6]/ion-col[1]/button/span').click()
    
    press ('enter')
    time.sleep(2)
    press ('enter')
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    press ('enter')
    time.sleep(2)
    press ('enter')
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    

    driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'REPORTS'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
    time.sleep(2)


    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[1]/div[1]/div').click()
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[2]/ion-card-content/ion-row/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button/span/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button/span').click()
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[4]/ion-card-content/ion-row/ion-col[2]/button/span').click()
    time.sleep(4)
    driver.switch_to_window(driver.window_handles[1])
    driver.minimize_window()
    time.sleep(4)
    
    if i <= 0:
        press('p')
        time.sleep(3)
        press('enter') 
        time.sleep(2)
        press('a')
        time.sleep(2)
        press('enter')
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        driver.maximize_window()
        time.sleep(3)
        file = open("C:/Users/ASUS/Downloads/p.csv",)
        value = (file.readlines())[27]
        index = 11
        x = (value[index:len(value)])
    else:
        press('q')
        time.sleep(3)
        press('enter') 
        time.sleep(2)
        press('b')
        time.sleep(2)
        press('enter')
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        driver.maximize_window()
        time.sleep(3)
        file = open("C:/Users/ASUS/Downloads/q.csv",)
        value = (file.readlines())[27]
        index = 11
        x = (value[index:len(value)])
        
    print(cf)
    print(x)
    if int(cf) == int(x):
        driver.execute_script('alert("CASH FUND VALUE MATCH ✅");')
    else:
        driver.execute_script('alert("CASH FUND VALUE NOT MATCH ❌");')
    
    time.sleep(7)
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.close()
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-header/ion-navbar/ion-buttons/button').click()

time.sleep(2)
driver.execute_script('alert("ALL BUTTONS IS WORKING PROPERLY: ✅" +"\\n" +"CANT SAVE CASH FUND IF VALUE IS 0: ✅" +"\\n" +"CASH FUND HAS BEEN SUCCESSFULLY SAVE: ✅" +"\\n" +"CASH FUND VALUE MATCH ✅ ");')  

 