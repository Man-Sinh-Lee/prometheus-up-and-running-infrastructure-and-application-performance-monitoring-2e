#!/usr/bin/env python3

import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')
SALES = Counter('hello_world_sales_euro_total',
        'Euros made serving Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        euros = random.random()
        SALES.inc(euros)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} euros.".format(euros).encode())

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('192.168.1.111', 8090), MyHandler)
    server.serve_forever()
