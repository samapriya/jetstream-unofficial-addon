import requests, json
from pprint import pprint
from urllib2 import Request, urlopen
import urllib
def jetaction(username=None,password=None,instid=None,act=None):
    resp = requests.post('https://use.jetstream-cloud.org/auth', data=json.dumps({'username':username, 'password': password}),
                         headers={'content-type':'application/json', 'accept':'application/json'})
    data = resp.json() #This gets token from the login
    response_body=json.load(urlopen(Request('https://use.jetstream-cloud.org/api/v2/instances',
                            headers={'content-type':'application/api', 'accept':'application/json', 'Authorization': 'Token %s' % data['token']})))
    i=0
    maxima=int(response_body['count'])
    while i<maxima:
        idn=response_body['results'][i]['id']
        instuuid=str(response_body['results'][i]['uuid'])
        iname=str(response_body['results'][i]['name'])
        identity=str(response_body['results'][i]['identity']['uuid'])
        provider=str(response_body['results'][i]['provider']['uuid'])
        i=i+1
        if int(idn)==int(instid):
            acts="'{"+'"action":'+'"'+act+'"}'+"'"
            headers = {
                'Authorization': 'Token %s' % data['token'],
                'Origin': 'https://use.jetstream-cloud.org',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
            }
            data='{"action":"stop"}' #Default action but is replaced by None is nothing is selected or whatever action is selected by user
            data=(data.replace("stop",act)) 
            print("Now performing action:" +str(act)+" on "+str(iname))
            uraction=('https://use.jetstream-cloud.org/api/v1/provider/'+str(provider)+'/identity/'+str(identity)+"/instance/"+str(instuuid)+'/action')
            exe=requests.post(uraction, headers=headers,data=data)
            if exe.status_code==200:
                print("Action succeeded")
                print(' ')
            elif exe.status_code==409:
                print("Action Conflict detected: Check action being called on instance")
                print(' ')
            else:
                print("Action failed check online at https://developer.mozilla.org/en-US/docs/Web/HTTP/Status "+str(exe.status_code))
                print(' ')
        else:
            print("Skipping Instance: "+str(iname))
