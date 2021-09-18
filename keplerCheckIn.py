import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from getpass import getpass
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
chromedriverPath = "/usr/local/bin/chromedriver"
web = webdriver.Chrome(
    '/Users/jruecke/code/python/chromedriver')
web.get("https://app.cleared4school.com/login")
print("Opened browser to https://app.cleared4school.com/login")
time.sleep(2)

email = "jasonrueckert@gmail.com"
password = ""

email_textbox = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-login/div[1]/div/div/div/div/form/div[1]/div/p/input')
email_textbox.send_keys(email)
print("Entered email")

password_textbox = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-login/div[1]/div/div/div/div/form/div[2]/div/p/input')
password_textbox.send_keys(password)
print("Entered password")

submitButton = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-login/div[1]/div/div/div/div/form/div[3]/div/input')
submitButton.submit()
print("Clicked Submit")
time.sleep(5)

dailyScreeningButton = web.find_element(
    By.XPATH, '//*[@id="collapseCardExample27594"]/div/a').click()
time.sleep(3)
print("Clicked Kepler button")
for i in range(16):
    web.find_element(By.XPATH, '//*[@id="content"]/div/app-daily-screening1/div/div/div/div/div/div/div[3]/div[1]/div[' + str(
        i+1) + ']/div[1]/div[3]/label/span').click()
    time.sleep(1)
    times = str(i + 1)
    print(f"Clicked 'No' button {times}  times")

acknowledge = web.find_element(By.XPATH, '//*[@id="ack-statement340"]').click()
sumbitButton = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-daily-screening1/div/div/div/div/div/div/div[3]/div[2]/div[3]/button').click()
print("Checked Acknowledge box")
# web.close()
print("Closed the browser")


gmail_user = 'phlacin@gmail.com'
gmail_password = '1975Waka1975'

sent_from = gmail_user
to = ['jasonrueckert@gmail.com', 'phlacin@gmail.com']
subject = 'Kep is checked in for school today'
body = 'Kepler has been successfully been Cleared4School'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong….", ex)
