import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HttpHelper:
    def __init__(self):
        self.url = 'https://localhost:7045'

    def doRequest(self, endpoint, method, headers=None, data=None):
        method = method.upper()
        print(self.url+endpoint)
        if method == "GET":
            return requests.get(self.url + endpoint, headers=headers, verify=False)
        elif method == "POST":
            return requests.post(self.url + endpoint, headers=headers, json=data, verify=False)
