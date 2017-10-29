from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='C:/Program Files/PhantomJS/bin/phantomjs')
#driver = webdriver.Chrome(executable_path='C:/Program Files/PhantomJS/bin/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5) #depois reduzir para 1s para entender a lógica
print(driver.find_element_by_id("content").text)
driver.close()
