

import requests


def sendFile(file):
    r = requests.post('http://47.113.225.179:80/fdfsfile/api', files={'file': file})
    return r
