import time

import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:6668')


    cnt = 1000

    while True:

        socket.send_string('test {}'.format(cnt))
        print('send {}'.format(cnt))
        cnt += 1
        time.sleep(1)


if __name__ == '__main__':
    run()