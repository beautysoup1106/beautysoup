import _thread
import ssl
import time
import timeit

import requests
import websocket

'''
HTTP请求数据时延
'''
# def get_orderbook():
#     orderbook = requests.get('https://api.gemini.com/v1/book/btcusd').json()
#     print(orderbook)
#
#
# n = 10
# latency = timeit.timeit('get_orderbook()', setup='from __main__ import get_orderbook', number=n) * 1.0 / n
# print('Latency is {} ms'.format(latency * 1000))


'''
websocket编程：连续发送消息的同时，也在不断的接收消息，不需要等待服务器完成请求完全回复之后，再进行下一个请求，即全双工
'''

# # 在接收到服务器发送消息时调用
# def on_message(ws, message):
#     print('Received: ' + message)
#
#
# # 在和服务器建立完成连接时调用
# def on_open(ws):
#     # 线程运行函数
#     def gao():
#         # 往服务器依次发送0-4，每次发完休息0.01s
#         for i in range(5):
#             time.sleep(0.01)
#             msg = '{0}'.format(i)
#             ws.send(msg)
#             print('Send: ' + msg)
#         # 休息1秒用于接收服务器回复的消息
#         time.sleep(10)
#
#         # 关闭websocket的连接
#         ws.close()
#         print('Websocket closed')
#         time.sleep(10)
#
#     # 在另一个线程运行gao()函数
#     _thread.start_new_thread(gao, ())
#
#
# if __name__ == '__main__':
#     # websocket.enableTrace(True)
#     ws = websocket.WebSocketApp('ws://echo.websocket.org/',
#                                 on_open=on_open,
#                                 on_message=on_message
#                                 )
#
#     ws.run_forever()
'''
双工示例
建立连接后，我们并没有向服务器发送任何消息，没有任何请求，但是服务器却源源不断的在向我们推送数据
缺点：请求和回复是异步的，会让程序的状态控制逻辑更加复杂
'''
count = 5


def on_message(ws, message):
    global count
    print(message)
    count -= 1
    # 接收了5次消息之后关闭websocket连接
    if count == 0:
        ws.close()


if __name__ == '__main__':
    ws = websocket.WebSocketApp(
        'wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=ture&offers=true',
        on_message=on_message
    )
    ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})
