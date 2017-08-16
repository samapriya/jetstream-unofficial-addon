import requests, json
from pprint import pprint
from urllib2 import Request, urlopen
def jetinstance(username=None,password=None):
    resp = requests.post('https://use.jetstream-cloud.org/auth', data=json.dumps({'username':username, 'password': password}),
                         headers={'content-type':'application/json', 'accept':'application/json'})
    data = resp.json() #This gets token from the login
    response_body=json.load(urlopen(Request('https://use.jetstream-cloud.org/api/v2/instances',
                            headers={'content-type':'application/api', 'accept':'application/json', 'Authorization': 'Token %s' % data['token']})))
    i=0
    maxima=int(response_body['count'])
    while i<maxima:
        idn=response_body['results'][i]['id']
        i=i+1
        ur='https://use.jetstream-cloud.org/api/v2/instances/'+str(idn)
        jsonList = json.load(urlopen(Request(ur,
                            headers={'content-type':'application/api', 'accept':'application/json', 'Authorization': 'Token %s' % data['token']})))
        print("Username :"+str(jsonList['user']['username']))
        print("Image name :"+str(jsonList['name']))
        print("Image ID :"+str(jsonList['id']))
        print("Image Usage :"+str(jsonList['usage']))
        print("Start Date :"+str(jsonList['start_date']))
        print("User Burn Rate :"+str(jsonList['allocation_source']['user_burn_rate']))
        print("Compute Allowed :"+str(jsonList['allocation_source']['compute_allowed']))
        print("Compute Used :"+str(jsonList['allocation_source']['compute_used']))
        print("Image Size :"+str(jsonList['size']['name']))
        print("Image Memory :"+str(jsonList['size']['mem']))
        print("Image CPU Cores :"+str(jsonList['size']['cpu']))
        print("Image UUID :"+str(jsonList['uuid']))
        print("Web Desktop Enabled :"+str(jsonList['web_desktop']))
        print("Shell Enabled :"+str(jsonList['shell']))
        print("VNC Enabled :"+str(jsonList['vnc']))
        print("Provider Name :"+str(jsonList['provider']['name']))
        print("Image Status :"+str(jsonList['status']))
        print("IP address :"+str(jsonList['ip_address']))
        print(' ')
