#!/usr/bin/python3
import hmac, hashlib
import json
import urllib
from urllib.request import urlopen, Request
import time

apikey=''
secret=''

def btrequest(uri):
    signeduri = uri + '&nonce={0}&apikey={1}'.format(str(int(time.time() * 1000)), apikey)
    headers = { 'Content-Type': 'Application/Json', 'apisign': hmac.new(secret.encode(), URL.format(realuri).encode(), hashlib.sha512).hexdigest() }
    req = Request(URL.format(realuri), headers=headers)
    response = urlopen(req).read().decode()
    parsed = json.loads(response)
    return parsed
    
if __name__ == '__main__':
    balance = '/account/getbalance?currency={0}'  
    print(btrequest(balance.format('btc')))
    
    
#now you can too communicate with the bittrex api
