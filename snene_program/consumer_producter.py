'''
普通爬虫爬取多个页面
一个页面爬完了，才会接着爬第二个页面
'''
import asyncio_program
import random

# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time=int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)
#
# main(['url_1','url_2','url_3','url_4'])

'''
协程对象(coroutine object)
协程的执行：
    1、通过wait调用：交出控制权，程序阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续
        await为同步调用，即函数结束之前，是不会触发下一次的调用的
        开发需要提前知道一个任务的哪个环节会造成I/O阻塞，然后把这个环节的代码异步化处理，并且通过
        await来标识在任务的该环节中断该任务执行，从而去执行下一个事件循环任务，这样可以充分利用CPU资源，
        避免CPU等待I/O造成CPU资源白白浪费。当之前的任务的那个环节I/O完成后，会调用回调函数告诉调度器
        执行完了，协程可以从await获取返回值，
        然后继续执行没有完成的剩余代码(注意：即使交出控制权的协程执行完毕任务后等待再次获取控制权完成任务，
        也必须等到事件循环到该协程才能获得继续控制权，不会由于该协程已经完成await任务就直接给它控制权)。
        因此，如果一个任务不涉及到网络或者磁盘I/O这种耗时操作，而只有CPU
        计算和内存I/O的操作时，协程并发的性能还不如单线程loop循环的性能高
        在协程中，程序员是系统的调度中心，我们已经知道哪里有I/O开销大的地方，主动放弃控制权给其他函数来执行
    2、通过asyncio.create_task()来创建任务，每一個新创建的协程对象都会自动调用add_done_callback()函数
        来添加一个回调函数，当协程对象的future状态启动时就会调用该回调函数，从而实现回调
        任务创建后很快就会被调度执行。main函数也可以理解为一个正常的task，要等这个task进入await状态，
        才会调度下一个task
    3、asyncio.run触发运行

'''

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# async def main(urls):
#     for url in urls:
#         await crawl_page(url)
#
#
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
'''
协程
用create_task来创建任务，任务创建后，很快就会被调度执行。
'''

# # async def crawl_page(url):
# #     print('crawling {}'.format(url))
# #     sleep_time = int(url.split('_')[-1])
# #     await asyncio.sleep(sleep_time)
# #     print('OK {}'.format(url))
# #
# #
# # async def main(urls):
# #     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
# #
# #     # for task in tasks:
# #     #     await task
# #     await asyncio.gather(*tasks)
#
#     tasks=[crawl_page(url) for url in urls]
#     asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    #或者
    # tasks=[asyncio.ensure_future(crawl_page(url)) for url inn urls]
    # asyncio.gather(*tasks)
#
# asyncio.run(main(['url_1','url_2','url_3','url_4']))

'''
生产者和消费者
'''


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val:{}'.format(id, val))
        await asyncio_program.sleep(1)


async def productor(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val:{}'.format(id, val))
        await asyncio_program.sleep(1)


async def main():
    queue = asyncio_program.Queue()
    consumer_1 = asyncio_program.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio_program.create_task(consumer(queue, 'consumer_2'))

    productor_1 = asyncio_program.create_task(productor(queue, 'productor_1'))
    productor_2 = asyncio_program.create_task(productor(queue, 'productor_2'))

    await asyncio_program.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio_program.gather(consumer_1, consumer_2, productor_1, productor_2, return_exceptions=True)


asyncio_program.run(main())
