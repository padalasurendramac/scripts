#!/bin/python3.6
import json
import ssl
import json
import sys
from os import environ
from os.path import isdir, isfile
from http import client
import sys
import pdb

class SocratesRestApiConfigData:
    def __init__(self, config_data):
        self.RACD = {
        'auth': {
            'API_URL': config_data['URL'],
            'header': {
                'Content-type': "application/json",
                'Cookie': "__cfduid=de94c8ea04e41f5b962db4dcb34f184081600743559"
             },
            'Request_Method': "POST",
            'API_method': "/channel-api/auth",
            'Body': {
                'appSecretCode': config_data['auth']['appSecretCode'],
                'username': config_data['auth']['username'],
                'phone': config_data['auth']['phone'],
                'email': config_data['auth']['email'],
                'responseFormat': "Raw"
            }
        },
        'ask': {
            'header': {
                'access-token': "",
                'Content-type': "application/json"
                },
            'Request_Method': "POST",
            'API_method': "/channel-api/ask",
            'Body': {
                "message": "When were you born?"
                }
            }
        }


def AskQuestion(ACD):
    Certs = ssl.SSLContext()
    Socrates_API_Https_Request = client.HTTPSConnection(
        ACD.RACD['auth'].get('API_URL'), 443, context=Certs, timeout=180)
    Socrates_API_Https_Request.request(
        ACD.RACD['auth'].get('Request_Method'), ACD.RACD['auth'].get('API_method                                                                                        '),
        json.dumps(ACD.RACD['auth'].get('Body')), ACD.RACD['auth'].get('header')                                                                                        )
    API_Repsonse = Socrates_API_Https_Request.getresponse()
    Response_string = (API_Repsonse.read().decode("utf-8"))
    try:
        J_response = json.loads(Response_string)
        return J_response
    except json.JSONDecodeError as e:
        Socrates_API_Https_Request.close
        Response_string = json.loads("{'success': 'false'}")
        return Response_string

# Main
#pdb.set_trace()
#username = sys.argv[1]
result = ({})
uat_kc = { 'URL': "uat-k-c.socrates.ai",
                'auth': {
                    'appSecretCode':"3c9039f4-2a40-48be-8df6-74b682da2b01",
                    'username': "randy.womack@kcc.com",
                    'phone': "888-555-1212",
                    'email': "randy.womack@kcc.com",
                    'responseFormat':"Raw"
                    }
                }

#print("Testing authentication for " + username)
uat_kc_instance = SocratesRestApiConfigData(uat_kc)
result = AskQuestion(uat_kc_instance)
if result['success'] =='true':
    print("OK - channel api is responding.")
    sys.exit(0)
else:
    print("CRITICAL - channel api is down")
    sys.exit(2)
