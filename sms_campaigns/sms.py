import plivo
import ConfigParser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = BASE_DIR + '/sms_campaigns/campaign.cfg'
if os.path.isfile(CONFIG_FILE):
    config = ConfigParser.ConfigParser()
    config.read(CONFIG_FILE)
    AUTH_ID = config.get('plivo','AUTH_ID')
    AUTH_TOKEN = config.get('plivo','AUTH_TOKEN')
    SRC_NUMBER = config.get('plivo', 'SRC_NUMBER')


def add_delimiter(contacts):
    return '<'.join(contacts)


def send_bulk_sms(contacts, msg):
    msg_unicode = msg
    auth_id = AUTH_ID
    auth_token = AUTH_TOKEN
    dst = add_delimiter(contacts)
    p = plivo.RestAPI(auth_id, auth_token)

    params = {
        'src': SRC_NUMBER,  # Sender's phone number with country code
        'dst': dst,  # Receiver's phone Number with country code
        'text': msg_unicode,  # Your SMS Text Message - English
        'url': "http://morning-ocean-4669.herokuapp.com/report/",
    # The URL to which with the status of the message is sent
        'method': 'GET'  # The method used to call the url
    }

    response = p.send_message(params)
    return response


def check_msg_status():
    pass