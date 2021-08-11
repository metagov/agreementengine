# import tweepy
# import pdb

# TWITTER_API_KEY="3gTUwkbzk73lOmE89yABbeFWG"
# TWITTER_API_SECRET_KEY="DuHhk91bITQIzRKmqJe0w8hCXSllNlNB424grAKcUB4pd9jsw5"
# TWITTER_ACCESS_TOKEN="1337163697836281857-TG7vLiZCI5oeWwILdDM2zmiwpRW6Sr"
# TWITTER_ACCESS_TOKEN_SECRET="EabxnU44yRPQvn0Jhj9Rk7Tw5Pwf98EQZyZ4PaqEXNZbg"

# auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
# auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth)

# try:
#     t = api.get_user('lukvmiasdfl')
#     print(t.id)
# except tweepy.error.TweepError as e:
#     if e.api_code == 50:
#         print('invalid user')

        
import requests

resp = requests.post(
    url='http://127.0.0.1:8000/api/internal/action/twitter.get-user-id',
    headers={'Content-Type': 'application/json', 'X-Metagov-Community': 'a9fa02a7-de85-47ba-8bc0-bac507b50150'},
    json={'parameters': {'screen_name': 'lukvmil'}}
).json()

if resp:
    user_id = resp
    requests.post(
        url='http://127.0.0.1:8000/api/internal/action/twitter.send-dm',
        headers={'Content-Type': 'application/json', 'X-Metagov-Community': 'a9fa02a7-de85-47ba-8bc0-bac507b50150'},
        json={'parameters': {'user_id': str(user_id), 'text': 'test'}}
    )
else:
    print('Could not find user')

