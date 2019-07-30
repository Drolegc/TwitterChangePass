#imap.gmail.com
#993
# hnksgdbcrpjaatyh

#<a href=3D"=
#https://twitter.com/i/redirect?url=3Dhttps%3A%2F%2Ftwitter.com%2Faccount%2F=
#confirm_email_reset%3Freset_type%3De%26user_id%3D3199491135%26token%3DTzDRV=
#hKucnfejf508sCXZzI0GW8QfSpRkSu9Hvr4Cfg%253D-1564465173103%26confirm_pending=
#_email%3D0%26token_version%3D0%26password_reset_cause%3Duser%26cn%3DcGFzc3d=
#vcmRfcmVzZXRfdjI%253D&amp;t=3D1+1564465173240&amp;cn=3DcGFzc3dvcmRfcmVzZXRf=
#djI%3D&amp;sig=3D5ad1ef5ef59a9ea7ddfc29877fe00462a4146fbe&amp;iid=3D44efa92=
#8d031495eb99e401f86af8004&amp;uid=3D3199491135&amp;nid=3D248+1393"

import imaplib
import base64
import os
import email
from bs4 import BeautifulSoup as bs

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

user_email = 'drolegc@gmail.com'
user_pass = 'hnksgdbcrpjaatyh'

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login(user_email,user_pass)

mail.select('Inbox')

result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
raw_email = email.message_from_bytes(data[0][1]) # here's the body, which is raw text of the whole email
#soup = bs(raw_email,'html5lib')
# including headers and alternate payloads
print(get_body(raw_email))
