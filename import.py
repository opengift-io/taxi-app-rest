# -*- coding:utf-8 -*-
__author__ = 'Gvammer'
import re
import requests, json
from requests.auth import HTTPBasicAuth

server = 'http://127.0.0.1:5000/'

f = open('worldcitiespop.txt')
head = True

country = {
    'title': 'Nigeria',
    'code': 'ng',
    'flag': 'https://flags.fmcdn.net/data/flags/w1160/ng.png'
}
auth = requests.auth.HTTPBasicAuth('admin', 'admin')
requests.delete(server + 'countries/', auth=auth)
requests.delete(server + 'cities/', auth=auth)

r = requests.post(server + 'countries/', data=country, auth=auth)
countryId = json.loads(r.content)['_id']

for s in f:
    if not head:
        s = s.split(',')

        if s[0] == 'ng':
            city = {
                'title': s[2],
                'code': re.sub('[^A-z0-9]', '_', s[1])
            }

            city['country'] = countryId

            requests.post(server + 'cities/', data=city, auth=auth)

    head = False

f.close()

