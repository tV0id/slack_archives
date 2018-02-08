import json

jsonfile = open('introductions/introductions_1518026373.json').read()
jsondata = json.loads(jsonfile)

htmldata = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Travis CI test</title>\n</head>\n<body>'
if jsondata['ok']:
    for message in jsondata['messages']:
        htmldata += '<div>\n<h1>' + message['user'] + '</h1>\n<p>' + message['text'] + '</p>\n</div>\n'

htmldata += '</body>\n</html>\n'
htmldata = htmldata.encode('utf-8').strip()
htmlfile = open('index.html', 'w')
htmlfile.write(htmldata)
htmlfile.close()
