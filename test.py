import requests
from requests.api import head

custom_headers = {
    'X-Metagov-Community': 'comm',
}
data = {
    
        'username': 'system'
}

while True:
    name = input('> ')
    x = requests.post(
        url='http://127.0.0.1:8000/api/internal/action/sourcecred.user-cred',
        headers=custom_headers,
        json={"parameters": {"username": name}}
    )

    print(x.text)