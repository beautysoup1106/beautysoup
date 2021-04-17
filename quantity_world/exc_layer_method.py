import base64
import datetime
import hashlib
import hmac
import json
import time

import requests

base_url = 'https://api.sandbox.gemini.com'
end_point = '/v1/order/new'
url = base_url + end_point

gemini_api_key = 'jfkdhfkshksjgdjgjgsjs'
gemini_api_secret = 'hgvfhdgydyfgj'.encode()

t = datetime.datetime.now()
payload_nonce = str(int(time.mktime(t.timetuple()) * 10000))

'''
nonce是个单调递增的整数，当某个后来的请求的nonce，比上个成功收到的请求的nonce小或者相等的时候，Gemini会拒绝
这次重复包请求。因为nonce的加入，加密后的同样订单的加密文档完全混乱，使得中间人无法通过发送同样的包来构造重复订单攻击。

timestamp在要求不是很严格的低频交易中，可以作为nonce存在。但是其类型为float，需要进行转换
但是高频交易中不适合。如，使用协程或者异步编程工具，数据或者程序可能并不是按照你想要的顺序发送给服务器，会出现timestamp
大的请求早发送。而且在网络传输中，包的抵达顺序也不定，这样如果多台机器对同一个仓位同一个API KEY进行操作，就会变得非常麻烦
'''
payload = {
    'request': '/v1/order/new',
    'nonce': payload_nonce,
    'symbol': 'btcusd',
    'amount': '5',
    'price': '3633.00',
    'side': 'buy',
    'type': 'exchange limit',
    'options': ['maker-or-cancel']
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
#对payload用私钥进行base64和sha384算法非对称加密，公钥可以解密
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = {
    'Content-Type': 'text/plain',
    'Content-length': '0',
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': 'no-cache'
}

response=requests.post(url,
                       data=None,
                       headers=request_headers)

new_order=response.json()
print(new_order)