from six.moves import urllib
import json
import asyncio

class Client:
    def __init__(self, endpoint, loop=None):
        self.endpoint = endpoint
        self.token = None
        self.headername = None
        self.loop = loop or asyncio.get_event_loop()

    def execute(self, query, variables={}):
        return self.loop.run_in_executor(None, lambda: self._send(query, variables))

    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            # print((e.read()))
            # print('')
            raise e
