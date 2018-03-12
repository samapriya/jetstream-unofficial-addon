import requests, json
from pprint import pprint
from urllib2 import Request, urlopen
def jetvolume(username=None,password=None):
    resp = requests.post('https://use.jetstream-cloud.org/auth', data=json.dumps({'username':username, 'password': password}),
                         headers={'content-type':'application/json', 'accept':'application/json'})
    data = resp.json() #This gets token from the login
    response_body=json.load(urlopen(Request('https://use.jetstream-cloud.org/api/v2/volumes',
                            headers={'content-type':'application/api', 'accept':'application/json', 'Authorization': 'Token %s' % data['token']})))
    i=0
    maxima=int(response_body['count'])
    while i<maxima:
        print("Username :"+str(response_body['results'][0]['user']['username']))
        print("Image name :"+str(response_body['results'][0]['name']))
        print("Start Date :"+str(response_body['results'][0]['start_date']))
        print("Image Size :"+str(response_body['results'][0]['size']))
        print("Provider Name :"+str(response_body['results'][0]['provider']['name']))
        print(' ')
        i=i+1
