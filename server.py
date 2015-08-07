from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

slackUrl = 'https://hooks.slack.com/services/XXXXXX'

@app.route('/')
def root():
        print 'ok'
        return 'ok'

@app.route('/github', methods=['POST'])
def github_webhook():
        d = request.get_data()
        j = json.loads(d)
        r = j['repository']['name']
        print '----'
        for c in j['commits']:
                msg = "%s on repo %s :\n '%s'\n%s " % (c['committer']['name'],r,c['message'],c['url'])
                print msg
                payload={"channel": "#activity","username": "github","text": msg}
                requests.post(slackUrl, json.dumps(payload), headers={'content-type': 'application/json'})
        return 'ok'

if __name__ == "__main__":
        app.run(host='0.0.0.0')