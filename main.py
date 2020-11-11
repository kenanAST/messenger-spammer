from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import details
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.messenger.com')

email_xpath = '/html/body/div/div/div[1]/div/div/div/div[1]/div/div[3]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[6]'
password_xpath = '/html/body/div/div/div[1]/div/div/div/div[1]/div/div[3]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[7]'
search_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input'
receiver_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul'
write_message_xpath = '/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div'
send_messsage_xpath = '/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a'


email = driver.find_element_by_xpath(email_xpath)
email.send_keys(details.email)

password = driver.find_element_by_xpath(password_xpath)
password.send_keys(details.password)
password.submit()


search = driver.find_element_by_xpath(search_xpath)
search.send_keys(details.receiver_name)
time.sleep(0.5)
receiver = driver.find_element_by_xpath(receiver_xpath)
receiver.click()


for i in range(details.number_of_spam):
    write_message = driver.find_element_by_xpath(write_message_xpath)
    write_message.send_keys( str(i+1) + '. ' + details.message)
    write_message.send_keys(u'\ue007')
