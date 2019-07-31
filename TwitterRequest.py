
import requests
from bs4 import BeautifulSoup as bs
LOGIN_URL = 'https://twitter.com/login'
RESTART_URL = 'https://twitter.com/account/begin_password_reset'
CONFIRM_URL = 'https://twitter.com/account/send_password_reset'

new_pass_url = ''
RESET_PASS = 'https://twitter.com/account/reset_password'


def printR(r):
    soup = bs(r.content,'html5lib')
    print('Status code: {}'.format(r.status_code))
    print(r.url)

form_data = {
    'authenticity_token':'',
    'account_identifier':'SOME EMAIL',
    
}

#Here Twitter use some id in the method_hint related with the account, but it works for others accounts
form_data_continue = {
    'authenticity_token': '',
    #'method_hint[1524856827]': 'device', #Can be an opcion with device and/or email
    'method_hint[132848851]': 'email',
    'method': '132848851', #id from the method choseen
}

form_data_end = {
    'authenticity_token': '',
    'password':'qwerty123',
    'password_confirmation':'qwerty123',
}

headers = {
    'Refer':RESTART_URL,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

print(':: Twitter Test :::')

with requests.Session() as s:
    
    r = s.get(RESTART_URL)
    
    printR(r)
    soup = bs(r.content,'html5lib')
    form_data['authenticity_token'] = soup.find('input',attrs={'name':'authenticity_token'})['value']
    
    r = s.post(RESTART_URL,data=form_data,headers=headers)
    printR(r)
    
    form_data_continue['authenticity_token'] = form_data['authenticity_token']

    r = s.post(CONFIRM_URL,data=form_data_continue,headers=headers)
    printR(r)
    
    print('::: NEW PASS :::')

    new_pass_url = raw_input('Insert token link (The link from de button in the email) \n')

    r = s.get(new_pass_url)
    printR(r)

    form_data_end['authenticity_token'] = form_data_continue['authenticity_token']
    headers['Refer'] = RESET_PASS

    r = s.post(RESET_PASS,data=form_data_end,headers=headers)
    printR(r)
    


