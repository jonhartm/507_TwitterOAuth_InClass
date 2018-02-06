from requests_oauthlib import OAuth1Session
import secret_data
import json

client_key = secret_data.CONSUMER_KEY
client_secret = secret_data.CONSUMER_SECRET

resource_owner_key = secret_data.ACCESS_KEY
resource_owner_secret = secret_data.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
r_json = json.loads(r.text)

for status in r_json['statuses']:
    print("@" + status['user']['screen_name'] + " says:")
    print(status['text'])
    print()


out = open('out.txt', 'w')
out.write(r.text);
