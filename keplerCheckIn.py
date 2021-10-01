#!/usr/bin/env python3
import smtplib
import sys
import os
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from getpass import getpass
import time

# Env Variables
login = os.environ.get("C4S_LOGIN")
password = os.environ.get("C4S_PASS")
gmail_address = os.environ.get("GMAIL_EMAIL")
gmail_pass = os.environ.get("GMAIL_PASS")

# login = sys.argv[1]
# password = sys.argv[2]
# gmail_address = sys.argv[3]
# gmail_pass = sys.argv[4]

confirmationTimeStamp = ""
confirmationErrorMessage = "Whoops, the confirmation did not work correctly."
log = []
bodyLog = ""
keplerMessage = ""
keplerSubject = ""

# Setup Selenium and open browser

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
chromedriverPath = "/usr/local/bin/chromedriver"
web = webdriver.Chrome(
    chromedriverPath, options=options)
web.get("https://app.cleared4school.com/login")
print("Opened browser to https://app.cleared4school.com/login")
log.append("Opened browser to https://app.cleared4school.com/login")
time.sleep(2)

# Fill out the attestation application
email_textbox = web.find_element(
    By.XPATH, '//*[@id = "content"]/div/app-login/div[1]/div/div/div/div/form/div[1]/div/p/input')
email_textbox.send_keys(login)
print("Entered email")
log.append("Entered email")

password_textbox = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-login/div[1]/div/div/div/div/form/div[2]/div/p/input')
password_textbox.send_keys(password)
print("Entered password")
log.append("Entered password")

submitButton = web.find_element(
    By.XPATH, '//*[@id="content"]/div/app-login/div[1]/div/div/div/div/form/div[3]/div/input')
submitButton.submit()
print("Clicked Submit")
log.append("Clicked Submit")
time.sleep(5)

dailyScreeningButtonX = web.find_element(
    By.XPATH, '//*[@id="collapseCardExample27594"]/div/a')
print(dailyScreeningButtonX.text)
log.append(dailyScreeningButtonX.text)

dailyScreeningButton = web.find_element(
    By.XPATH, '//*[@id="collapseCardExample27594"]/div/a').click()
time.sleep(3)
for i in range(16):
    web.find_element(By.XPATH, '//*[@id="content"]/div/app-daily-screening1/div/div/div/div/div/div/div[3]/div[1]/div[' + str(
        i+1) + ']/div[1]/div[3]/label/span').click()
    time.sleep(1)
    times = str(i + 1)
    # print(f"Clicked 'No' button {times} times")

log.append(f"Clicked 'No' button 16 times")

acknowledge = web.find_element(
    By.XPATH, '//*[@id="ack-statement340"]').click()
log.append("Clicked the Acknowledge box")

# def submitAttestation():
#     submitButton = web.find_element(
#         By.XPATH, '//*[@id="content"]/div/app-daily-screening1/div/div/div/div/div/div/div[3]/div[2]/div[3]/button').click()
#     log.append("Clicked the FINAL Submit button")

# submitAttestation()

time.sleep(3)

confirmationsMessage = web.find_element_by_xpath(
    '//*[@id = "content"]/div/app-daily-screening1/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/p[1]').text

if (confirmationsMessage) == "Based on your responses, you are Cleared4School.":
    confirmationTimeStamp = web.find_element_by_xpath(
        '//*[@id="content"]/div/app-daily-screening1/div/div/div/div/div/div/div[2]/div[1]/p[2]').text
    keplerMessage = f"Kepler has been successfully Cleared4School on {confirmationTimeStamp}"
    print(keplerMessage)
    keplerSubject = "Check-In Status: Confirmed"
    log.append(keplerMessage)
else:
    keplerMessage = "ERROR: Kepler has NOT been successfully been Cleared4School yet. Try again."
    print(keplerMessage)
    keplerSubject = "Check-In Status: NOT Confirmed"
    log.append(keplerMessage)

# web.close()
print("Closed the browser")
log.append("Closed the browser")

# Convert log list to string

bodyLog = '\n'.join(log)

# Send an email that the student attestation has been submitted


def email_alert(subject, body, to, cc):
    user = gmail_address
    password = gmail_pass

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['cc'] = cc
    msg['from'] = "Kepler Bot"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


email_alert(keplerSubject, bodyLog,
            "phlacin@gmail.com", "")
