#!/usr/bin/env python
# coding: utf-8

# vdcinfo is a helper script to get virtual data center data and parse it to readable and "greppable" format

import os,json,requests

# You will need to have the IONOS_TOKEN environent variable set for this to work
headers = {"Authorization": "Bearer "+os.environ["IONOS_TOKEN"]}
endpoint="https://api.ionos.com/cloudapi/v6/datacenters?depth=10&limit=100"
data=requests.get(endpoint, headers=headers).json()

# ignore some verbose values that are most likely of no intrest. adapt the list if they are.
IGNORE_KEYS=["href","etag","lastModifiedByUserId","createdByUserId"]

# recursive function to walk throgh the nested configuration data. The item[].type
# and properties.name are used as keys in the path for better searchability
def recfind(v,cp=[]):
    if type(v) in (type(0), str):
        print("/".join(cp),"=",repr(v))
    elif type(v)==dict:
        for key,c in v.items():
            if key == "items":
                try:
                    key=c[0]["type"]
                except:
                    pass
            elif key in IGNORE_KEYS:
                continue
            recfind(c,cp+[key])
    elif type(v)==list:
        for key,c in enumerate(v):
            try:
                key=c["properties"]["name"].replace("/","_")
            except:
                pass
            recfind(c,cp+[str(key)])

recfind(data)




