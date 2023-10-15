"""
Copyright (c) 2023 Gregor Gottschewski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import requests
import json
import argparse

from mitmproxy import http
from mitmproxy.tools.main import mitmdump

parser = argparse.ArgumentParser(
    prog="MitmFox Client",
    description="Runs mitmproxy and sends responses and requests to a MitmFox Server",
    epilog="PLEASE READ THE LICENSE BEFORE USING",
)

parser.add_argument("server_address", type=str, help="address of MitmFox server")
args = parser.parse_args()

server_address = args.server_address


def get_body_decoded(b: bytes):
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return ""


def send_to_server(server: str, json_data: dict):
    requests.post(server, json=json_data)


def response(flow: http.HTTPFlow) -> None:
    response_body = get_body_decoded(flow.response.content)
    request_body = get_body_decoded(flow.request.content)

    body = {
        "url": flow.request.url,
        "method": flow.request.method,
        "response_body": response_body,
        "request_body": request_body,
        "status_code": flow.response.status_code,
        "response_headers": json.dumps(dict(flow.response.headers)),
        "request_headers": json.dumps(dict(flow.request.headers))
    }
    send_to_server(server_address, body)


if __name__ == '__main__':
    server_address = server_address
    mitmdump(['-s', __file__])
