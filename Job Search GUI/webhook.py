import requests
import json 

#Ethan Burchett Summer 2021
#This defines a simple webhook, you need to initalize this with the input data(what type? ), then has method: 
#method: post request sends json data to zapier

#example: require zap_hook_url and data
# data must be in json format

            #hook = webhook.Webhook(data,zap_hook_url)                   <----- constructor s
            #hook.postRequest()


class Webhook:
    def __init__(self, data, zap_hook_url):
        self.data = data
        self.zap_hook_url = zap_hook_url
        

    def postRequest(self):    #remember that you must use the self as an argument
        r = requests.post(self.zap_hook_url, data=json.dumps(self.data), headers={'Content-Type': 'application/json'})

