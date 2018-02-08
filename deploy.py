#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import json

jsonfile = open('introductions/introductions_1518026373.json').read()
jsondata = json.loads(jsonfile)

# the HTML header
head = open('templates/head.html').read()
header = open('templates/header.html').read()
htmldata = head + header

if jsondata['ok']:
    for message in jsondata['messages']:
        htmldata += '<div>\n<h1>' + message['user'] + '</h1>\n<p>' + message['text'] + '</p>\n</div>\n'

htmldata += '</body>\n</html>\n'
htmldata = htmldata.encode('utf-8').strip()
htmlfile = open('pages/index.html', 'w')
htmlfile.write(htmldata)
htmlfile.close()
