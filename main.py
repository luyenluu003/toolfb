import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def login(username,password,token):
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com')
    username_input = driver.find_element(By.ID, 'email')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys(password)
    login_button  = driver.find_element(By.NAME, 'login')
    login_button.click()
    try:
        password_input = driver.find_element(By.ID, 'pass')
        if(password_input):
            return "WRONG"
    except:
        pass
    try:
        code_input = driver.find_element(By.ID, 'approvals_code')
        code_input.send_keys(token)
        try:
            code_input = driver.find_element(By.ID, 'approvals_code')
            if(code_input):
                return "WRONG"
        except:
            pass
        submit_button = driver.find_element(By.ID, 'checkpointSubmitButton')
        submit_button.click()
    except:
        pass
    for i in range(8):
        if i == 7:
            return "CheckPoint"
        current_url = driver.current_url
        if "checkpoint" in current_url:
            submit_button = driver.find_element(By.ID, 'checkpointSubmitButton')
            submit_button.click()
        else:
            break
    time.sleep(100)
username = "10005254212728"
password = "A@!ToiLaToi123"
key = "G6SVIVXYPT7MOEDVQLIMJPWHPVIIQ6BL"
response = requests.get(f"https://2fa.live/tok/{key}")
data = response.json()
token = data["token"]
print(login(username, password,token))
def read_accounts(file_path):
    accounts = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            accounts.append(parts)
    return accounts

file_path = "account.txt"
accounts = read_accounts(file_path)
usernames = ""
passwords = ""
tokens = ""
for account in accounts:
    username = account[0]
    password = account[1]
    token = account[2]
    usernames.append(username)
    passwords.append(password)
    tokens.append(token)