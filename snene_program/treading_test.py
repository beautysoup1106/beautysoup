'''
并发编程的两种形式：Threading(线程)和asyncio(协程)
线程:操作系统做主，在适当的时候做线程切换，不需要程序员做任何切换操作处理
    容易出现race condition即资源竞争。线程数量可以自己定义，但并不是
    越多越好，因为线程的创建、维护和删除也会有一定的开销。
    python的并发，是通过多线程的切换完成的。GIL的存在，使得同一时刻，主程序只允许有一个
    线程执行。但在进行I/O操作时，如果一个线程被block了，GIL就会被释放，从而
    让另一个线程能够继续执行
协程：必须得到任务可以切换的通知，才可以进行任务切换，不会出现资源竞争
'''
import concurrent.futures
import time
from concurrent import futures

import requests


def download_one(url):
    try:
        resp = requests.get(url)
    except (ConnectionError,TimeoutError,requests.exceptions.HTTPError) as e:
        print('get resource failed')

    else:
        print('Read {} from {}'.format(len(resp.content), url))

#方式一

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # with futures.ProcessPoolExecutor(5) as executor:
    #     省略workers参数，系统会自动返回CPU的数量作为可以进行调用的进程数
    #     with futures.ProcessPoolExecutor() as executor:
       try:
            executor.map(download_one, sites)
       except concurrent.futures.TimeoutError as e:
           print('Time out')

#方式二
def download_all1(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do=[]
        for site in sites:
            future =executor.submit(download_one,site)
            to_do.append(future)
        #future 列表中每个future完成的顺序，取决于系统的调度和每个future的执行时间
        try:
            for future in concurrent.futures.as_completed(to_do):
                future.result()
        except (TimeoutError,concurrent.futures.CancelledError)as e:
            print('error ocurred')

def main():
    sites = [
        'https://blog.csdn.net/caimouse/article/details/77869636',
        'http://www.jsphp.net/python/show-24-214-1.html',
        'https://blog.csdn.net/weixin_43533825/article/details/89155648',
        'https://www.cnblogs.com/shiqi17/p/9694938.html',
        'https://www.runoob.com/python/func-number-log.html',
        'https://www.runoob.com/python/python-tutorial.html',
        'https://www.cnblogs.com/xshrim/p/4077394.html',
        'https://www.cnblogs.com/shiqi17/p/9694938.html'
    ]
    start_time = time.perf_counter()
    download_all1(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


'''
多进程要放在主函数中进行
An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
'''
if __name__ == '__main__':
    main()
