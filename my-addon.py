import mitmproxy.http
from mitmproxy import ctx
import requests 
 
class Counter:
    def __init__(self):
        self.num = 0
 
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.pretty_url.endswith('.mp3'):
            ctx.log.info(flow.request.pretty_url)
            r = requests.get(flow.request.pretty_url, allow_redirects=True)
            fileName = flow.request.pretty_url.split('/')[-1]
            open(fileName, 'wb').write(r.content)
addons = [
    Counter()
]