import tweepy
import json
import requests
import sched
import time

with open('apikeys.json', 'r') as f:
    keys = json.load(f)

# sending keys to authenticator
auth = tweepy.OAuthHandler(
    keys['API key'], 
    keys['API key secret'])

auth.set_access_token(
    keys['Access token'], 
    keys['Acess token secret'])

api = tweepy.API(auth)

last_status_parsed = int(keys['Last status parsed'])

cursor = tweepy.Cursor(
    api.mentions_timeline,
    tweet_mode="extended",
    since_id=last_status_parsed, 
    count=200
)

s = sched.scheduler(time.time, time.sleep)

def scheduled_update(sc):
    global last_status_parsed
    s.enter(60, 1, scheduled_update, (sc,))
    before = time.time()

    for status in cursor.items():
        print(f"Received tweet #{status.id}, forwarding...")

        requests.post(url='http://127.0.0.1:5000/TSC', json=status._json)

        if status.id > last_status_parsed:
            last_status_parsed = status.id
            keys['Last status parsed'] = str(status.id)
            with open('apikeys.json', 'w') as f:
                json.dump(keys, f, indent=2)

s.enter(0, 1, scheduled_update, (s,))
s.run()