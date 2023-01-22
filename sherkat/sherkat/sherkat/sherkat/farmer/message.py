#!/usr/bin/env python
from email import header
from urllib import response
from kavenegar import *
from farmer.celery import app

# API_KEY = 'your_api_key'
# def sendMessage():
#     try:
#         import json
#     except ImportError:
#         import simplejson as json
        
#     try:
#         api = KavenegarAPI(API_KEY)
#         params = {
#             'sender': '10004346',
#             'receptor': '{Your Phone Number}',
#             'message': 'Kaveh specialized Web service '
#         }

#         response = api.verify_lookup(params)
#         print str(response)

#     except APIException as e:
#         print(e)
#     except HTTPException as e:
#         print(e)


API_KEY = 'your_api_key'
@app.task
def sendMessage(mobile, sms_type):
      api = KavenegarAPI(API_KEY)
      data = {
             'sender': '10004346',
             'receptor': '{Your Phone Number}',
             'message': 'Kaveh specialized Web service'
         }
      txt =data.get(sms_type)
      payload ={"from": "30000004346", "to": mobile, "txt": str(txt)}
      headers ={"Content-Type": "application/json"}
      response = requests.request("POST", url=SMS_URL, headers=headers, data=json.dumps(payload))
      print(response)