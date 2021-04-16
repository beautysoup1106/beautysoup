# for x in range(10000000):
#     f=open('test.txt','w')
#     f.write('hello')
import gc

# gc.collect()
from contextlib import contextmanager

# import DBClient as DBClient

'''
上下文管理器：能够帮助你自动分配并且释放资源。更加灵活，适用于大型的系统开发
with语句的使用可以简化代码，有效避免资源泄漏的发生

用类创建上下文管理器时，必须保证这个类包括方法__enter__（返回被管理的资源）
和 __exit__（释放、清理资源的操作，如果需要处理异常，可以在此添加。如果确认异常已经处理，则需返回
Ture，否则，异常仍然会被抛出）。
'''


# for x in range(2):
#     with open('text.txt','w') as f:
#         f.write('hello')

class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        # if self.file:
        #     self.file.close()
        if exc_type:
            print(f'exc_type:{exc_type}')
            print(f'exc_val:{exc_val}')
            print(f'exc_traceback:{exc_tb}')
            print('excption handled')
        return True


# with FileManager('text.txt','w') as f:
#     print('ready to write to file')
#     f.write('hello world')

with FileManager('text.txt', 'w') as f:
    raise Exception('exception raised').with_traceback(None)

'''
上下文管理器：数据库连接操作
'''

# class DBConnectionManager:
#     def __init__(self,hostname,port):
#         self.hostname=hostname
#         self.port=port
#         self.connection=None
#
#     def __enter__(self):
#         self.connection=DBClient(self.hostname,self.port)
#         return self.connection
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.close()
#
# with DBConnectionManager('localhost','8080') as db_client:
#     pass

'''
基于生成器的上下文管理器：不用再定义enter和exit方法，值需要加上上装饰器@contextmanager就可以
更加方便简洁，适用于中小型程序
'''


@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manager('test.txt', 'w') as f:
    f.write('hello world')
