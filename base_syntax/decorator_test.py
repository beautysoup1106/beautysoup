'''
简单装饰器
'''
import functools
import time


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper

@my_decorator
def greet():
    print("hello world")
#原始调用无需@装饰器名
# greet=my_decorator(greet)
# greet()
#wrapper of decorator
#hello world


#优雅调用，在被装饰函数前加@装饰器名语法糖，就相当于前面的greet=my_decorator(greet)

greet()


'''
带参数的装饰器:被装饰函数需要传参，在装饰器函数上加响应的参数，不定类型和不定长参数用无名参数*args 和关键字参数**kwargs
'''
def repeat(num):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args,**kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)

greet('hello world')


'''
内置装饰器(functools.wrap)：保留原函数的元信息
意义：多个函数被同一个装饰器装饰，如果出错了，能保留原函数的元信息，那么就可以知道具体是哪个函数出错了
因为多个函数用同一个装饰器装饰，这么多函数就都会被装饰器中的wrapper函数取代，用__name__查看，都是wrapper
'''

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('wrapper of decorator')
        func(*args,**kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)


print(greet.__name__)

'''
类装饰器:主要依赖于__call__()函数。每当调一个类的实例时，该函数就会被执行一次
'''
class count():
    def __init__(self,func):
        self.func=func
        self.num_calls=0

    def __call__(self, *args, **kwargs):
        self.num_calls+=1
        print('num of calls is {}'.format(self.num_calls))
        return self.func(*args,**kwargs)

@count
def example():
    print('hello world')

example()
example()
example()

'''
装饰器的嵌套:多层装饰器
'''
def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('execute decorator1')
        func(*args,**kwargs)
    return wrapper

def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('execute decorator2')
        func(*args,**kwargs)
    return wrapper

@my_decorator1
@my_decorator2
def greet(message):
    print(message)

'''
104到107行，相当于执行了greet=my_decorator1(my_decorator2(greet))
执行my_decorator2(greet),加载装饰函数wrapper2至内存中，将装饰器返回值wrapper2函数返回，wrapper2函数作为参数，
接下来，相当于执行my_decorator1(wrapper2),加载装饰器函数wrapper1至内存后，返回wrapper1.此时变量greet就相当于
wrapper1函数。调用greet(),就相当于调用wrapper1函数，wrapper1中有wrapper2函数的调用，wrapper2函数中又有被装饰
函数greet的调用。所有相当于调用wrapper1函数，执行函数体中wrapper2函数调用前的函数体，再执行wrapper1函数体中位于
greet调用前的函数体，然后执行greet函数体，之后执行wrapper2函数中位于greet函数调用之后的函数体，最后调用wrapper1
函数体中位于wrapper2函数调用之后的函数体


'''
greet('hello world')

'''
装饰器用法-身份认证
'''
def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        rquest=args[0]
        check_user_logged_in=0
        if check_user_logged_in:
            return func(*args,**kwargs)
        else:
            raise Exception('Authentication failed')

    return wrapper

@authenticate
def post_comment(request,s=3):
    pass

'''
装饰器用法-日志记录
'''
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        res=func(*args,**kwargs)
        end_time=time.perf_counter()
        print('{} took {} ms'.format(func.__name__,(end_time-start_time)*1000))
        return res
    return wrapper

@log_execution_time
def calculate_similarity(items):
    pass


'''
装饰器用法-输入合理性校验
'''

def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        '''输入合理性校验'''

        func()

    return wrapper()

@validation_check
def neutral_network_trainning():
    pass

'''
装饰器用法-缓存 LRUcache
'''

@functools.lru_cache
def check():
    pass
'''
工作当中，如果是二次开发，在原来的需求基础之上做优化，原逻辑不需要修改的情况下，只需要增加新的业务场景的
时候，装饰器就能运用。不动原来的逻辑，增加程序的健壮性
'''

