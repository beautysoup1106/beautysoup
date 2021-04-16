'''
async with异步上下文管理器，指的是能够在enter和exit方法处暂停执行的
上下文管理器，而且async with 必须要放在saync函数中
'''
import asyncio
import concurrent.futures
import multiprocessing
import time

import aiohttp


# async def download_one(url):
#     async with aiohttp.ClientSession(
#             headers={'User-Agent': 'test'}, connector=aiohttp.TCPConnector(ssl=False)
#     ) as session:
#         async with session.get(url) as response:
#             print('Read {} from {}'.format(response.content_length,url))
#
#
# async def download_all(sites):
#     tasks=[asyncio.create_task(download_one(site)) for site in sites]
#     await asyncio.gather(*tasks)
#
# def main():
#     sites = [
#         'https://blog.csdn.net/caimouse/article/details/77869636',
#         'http://www.jsphp.net/python/show-24-214-1.html',
#         'https://blog.csdn.net/weixin_43533825/article/details/89155648',
#         'https://www.cnblogs.com/shiqi17/p/9694938.html',
#         'https://www.runoob.com/python/func-number-log.html',
#         'https://www.runoob.com/python/python-tutorial.html',
#         'https://www.cnblogs.com/xshrim/p/4077394.html',
#         'https://www.cnblogs.com/shiqi17/p/9694938.html'
#     ]
#     start_time=time.perf_counter()
#     asyncio.run(download_all(sites))
#     end_time=time.perf_counter()
#
#     print('Download {} sites in {} seconds'.format(len(sites),end_time-start_time))

'''
CPU多进程方式(6.8291628)
'''
def cpu_bound(numbers):
    print(sum(i * i for i in range(numbers)))



def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    #with concurrent.futures.ProcessPoolExecutor() as executor:
    # with multiprocessing.Pool() as executor:
    #     executor.map(cpu_bound,numbers)
    # calculate_sum(numbers)
    asyncio.run(calculate_sum(numbers))
    end_time=time.perf_counter()

    print('Duration {} seconds'.format(end_time-start_time))

'''
多线程方式（20.2873567）
'''
def calculate_sum(numbers):

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound,numbers)
'''
异步方式（19.4278574）
'''
async def cpu_bound(number):
    print(sum(i*i for i in range(number)))

async def calculate_sum(numbers):
    tasks=[asyncio.create_task(cpu_bound(number)) for number in numbers ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    main()
