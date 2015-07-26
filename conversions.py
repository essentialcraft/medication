#!/usr/bin/env python

import json

in_file = open('data.json', 'r')
data = json.load(in_file)


# lbs / 2.2046
def poundsToKilo(pounds):
    print 'Begin converting %s\n' % pounds
    units = float(pounds) / data.get('conversions').get('lbto')
    return units

def returnOnHand(onHand):
    return "%s grams" % onHand
    

def findTag(data, key):
    for i in data:
        for j in i:
                if j["Key"] == key:
                        return j["Value"]

def listOrDict(data):
    if isinstance(data, dict):
        print 'dict'
        return data.get('instanceId')
    elif isinstance(data, list):
        print 'list'


in_file.close()