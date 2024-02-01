import requests 
from urllib.parse import quote

PHONE_NUMBER = ' 014996484378'
CALL_BOT_API_KEY = ''

message = '''
olá tudo bem ?
'''

requests.get (
    url=f' https://api.callbot.com/whatsapp.php\
        ?phone={PHONE_NUMBER}\
        &text={quote(message)}\
        &apikey={CALL_BOT_API_KEY}'

)