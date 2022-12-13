import requests as r
import json
import sys
import os
import time
import random
import csv
import names
import random
import string

def main():

    URL = 'https://www.littleburgundyshoes.com/account/login#register'
    fname = names.get_first_name()
    lname = names.get_last_name()
    email = fname + "." + lname + "@supcanada21.com"
    pw = 'Scruffy2012!'
    #gender = '<option value="Male">Male</option>': 'Male'

    payload = {
        'mode': 'register',
        'FirstName': fname,
        'LastName': lname,
        'Email': email,
        'Password': pw,
        'Gender': '',
        'Password2': pw, 
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"'
    }

    s = r.Session()
    req = s.post(URL, headers=headers, data=payload)
    time.sleep(2)
    print(req.text)
    print(req.url)
    
main()
