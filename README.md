# TwitterChangePass

TwitterChangePass is a script in python to change the password of a Twitter account using web-scraping

The script asks for the email linked to the twitter account and then 
you need the link from the bottom that is in your new email sent it from Twitter

Once the enter key its pressed,the script change the old password for qwerty123


SOME EMAIL: example@example.com
Status code: 200
https://twitter.com/account/begin_password_reset
Status code: 200
https://twitter.com/account/send_password_reset
Status code: 200
https://twitter.com/account/confirm_pin_reset
::: NEW PASS :::
Insert token link (The link from de button in the email) 
https://twitter.com/i/redirect?url=https-link-from-email
Status code: 200
https://twitter.com/account/reset_password
Status code: 200
https://twitter.com/account/password_reset_complete

