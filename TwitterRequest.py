#https://twitter.com/login?prefetchTimestamp=1564457669471

#PASS EMAIL inxlkadxqhwkhovs

#Primero - intentar logearnos

#session[username_or_email]: drolegc@gmail.com
#session[password]: 093364252
#authenticity_token: 1548968d6fa7c8f15628e712450613b677889230

import requests
from bs4 import BeautifulSoup as bs
LOGIN_URL = 'https://twitter.com/login'
RESTART_URL = 'https://twitter.com/account/begin_password_reset'
CONFIRM_URL = 'https://twitter.com/account/send_password_reset'

RESTABLECER_PASS_URL = 'https://twitter.com/i/redirect?url=https%3A%2F%2Ftwitter.com%2Faccount%2Fconfirm_email_reset%3Freset_type%3De%26user_id%3D1156326580291100674%26token%3Dbz4WgoWsWzJvtAUy1UbDJXf9oQBuvR_p8tJvzF8GQkY%253D-1564525099795%26confirm_pending_email%3D0%26token_version%3D0%26password_reset_cause%3Duser%26cn%3DcGFzc3dvcmRfcmVzZXRfdjI%253D&t=1+1564525099806&cn=cGFzc3dvcmRfcmVzZXRfdjI%3D&sig=58ce54dc4514d7441763f28f0cb4cbe0d122c089&iid=1e2ae650d5294b4bb807e6e26e1a93c0&uid=1156326580291100674&nid=248+1393'
RESET_PASS = 'https://twitter.com/account/reset_password'

#Los datos que necesitaremos en el formulario

def printR(r):
    soup = bs(r.content,'html5lib')
    print('Status code: {}'.format(r.status_code))
    print(r.url)

form_data = {
    'authenticity_token':'',
    'account_identifier':'tucartel.uruguay@gmail.com',
    #authenticity_token lo obtenemos del html
}

form_data_continue = {
    'authenticity_token': '',
    #'method_hint[1524856827]': 'device',
    'method_hint[132848851]': 'email',
    'method': '132848851', #EL METODO ELEJIDO
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
    
    r = s.get(RESTABLECER_PASS_URL)
    printR(r)

    form_data_end['authenticity_token'] = form_data_continue['authenticity_token']
    headers['Refer'] = RESET_PASS

    r = s.post(RESET_PASS,data=form_data_end,headers=headers)
    printR(r)
    

#authenticity_token: 08943f88d9864107a1bbd4973dd82e3713e34cef
#method_hint[1524856827]: device
#method_hint[109976781]: email
#method: 109976781 EL METODO ELEJIDO

#Buscar el link en el email mandado


