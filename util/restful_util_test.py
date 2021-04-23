import requests
from websocket import create_connection


class Conmmon(object):
    def __init__(self, url_root, api_type):

        if api_type == 'ws':
            self.ws = create_connection(url_root)
        elif api_type == 'http':
            self.ws = 'null'
            self.url_root = url_root

    def send(self, params):
        self.ws.send(params)
        res = self.ws.recv()
        return res

    def __del__(self):
        if self.ws != 'null':
            self.ws.close()

    def get(self, uri, params):

        if params is not None:
            url = self.url_root + uri + params
        else:
            url = self.url_root + uri
        res = requests.get(url)
        return res
    def post(self,uri,params=None):
        url=self.url_root+uri
        if params is not None:
            res=requests.post(url,params)
        else:
            res=requests.post(url)

        return res

    def put(self,uri,params=None):
        url=self.url_root+uri
        if params is not None:
            res=requests.put(url,data=params)
        else:
            res=requests.put(url)

        return res

    def delete(self,uri,params=None):
        url=self.url_root+uri
        if params is not None:
            res=requests.delete(url,data=params)

        else:

            res=requests.put(url)

        return res