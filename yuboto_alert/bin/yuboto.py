# stsimb may 2017
import sys,os
import json
import urllib
from urllib2 import urlopen, URLError, HTTPError

SPLUNK_HOME = os.environ.get("SPLUNK_HOME")
WHL_DIR = SPLUNK_HOME + "/etc/apps/yuboto_alert/bin/"

for filename in os.listdir(WHL_DIR):
    if filename.endswith(".whl"):
        sys.path.append(WHL_DIR + filename)

def send_message(settings):
    print >> sys.stderr, "DEBUG Sending message with settings %s" % settings

    yuboto = "https://services.yuboto.com/web2sms/api/v2/smsc.aspx"
    api_key = settings.get('apikey')
    sender = settings.get('sender')
    rcpt = settings.get('tonumber')
    text = settings.get('message')

    numbers_list = rcpt.split(",")
    for number in numbers_list:
        print >> sys.stderr, "INFO Sending SMS via Yuboto from %s to %s with text=%s" % (sender, rcpt, text)
        params = urllib.urlencode({
                                    "api_key" : api_key,
                                    "action"  : "send",
                                    "from"    : sender,
                                    "to"      : rcpt,
                                    "text"    : text
                                 })
        try:
            response = urlopen(yuboto, params)
        except HTTPError as e:
            print >> sys.stderr, "FATAL The server could not fulfill the request, error code %s" % e.code
            return False
        except URLError as e:
            if hasattr(e, 'reason'):
                print >> sys.stderr, "FATAL We failed to reach %s. Error: %s" % (yuboto, e.reason)
                return False
            elif hasattr(e, 'code'):
                print >> sys.stderr, "FATAL The server could not fulfill the request with error code: " % e.code
                return False
        else:
            # everything is fine
            #print >> sys.stderr, "INFO Sent Yuboto SMS message with response=%s" % response.getcode()
            return True

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        if not send_message(payload.get('configuration')):
            print >> sys.stderr, "FATAL Failed trying to send SMS Message via Yuboto."
            sys.exit(2)
        else:
            print >> sys.stderr, "INFO SMS Message successfully sent via Yuboto."
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)."
        sys.exit(1)
