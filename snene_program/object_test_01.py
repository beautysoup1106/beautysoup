'''
面向对象设计四要素：类，对象，属性，方法（类时一群有着相同属性和函数的对象的集合）
__init函数，类加载，对象初始化的时候就会被调用的函数
__变量名；私有属性，不希望在类的函数之外被访问和修改
类中定义常量：在类中，和函数并列的声明并赋值，一般用全大写表示，类中直接使用self.变量名或者类外使用Entity.变量名用

类方法：cls参数，最常用的方法是实现不同的构造__init__构造函数
静态方法：无特殊参数，与类没有什么关联
'''

# class Document():
#     WELCOME_STR='welcome !The context for this book is {}'
#     def __init__(self,title, author, context):
#         print('The init function called')
#         self.title=title
#         self.author=author
#         self.__context=context
#
#     @classmethod
#     def create_empty_book(cls,title,author):
#         return cls(title=title,author=author,context='nothing')
#
#     def get_context_length(self):
#         return len(self.__context)
#
#     @staticmethod
#     def get_welcome(context):
#         return Document.WELCOME_STR.format(context)
#
# emputy_book=Document.create_empty_book('what Every Man Thinks About from Sex','professor Sheridan Simove')
#
# print(emputy_book.get_context_length())
# print(emputy_book.get_welcome('indeed nothing'))
from abc import ABCMeta, abstractmethod

'''
类的继承:
经典类：python2中默认都是，但定义时显式继承了object类的也为新式类  继承关系搜索顺序  深度优先：从左找到头，再从右找到头
       
新式类：python3 继承关系搜索顺序 广度优先，如果形成了菱形结构，则只找到倒数第二层


'''
class Test():
    def __init__(self):
        print('enter Test')
        print('leave Test')

class Test1(Test):
    def __init__(self):
        print('enter Test1')
        super().__init__()
        print('leave Test1')
class Test2(Test):
    def __init__(self):
        print('enter Test2')
        super().__init__()
        print('leave Test2')

class A1(Test):
    def __init__(self):
        print('enter A1')
        super().__init__()
        print('leave A1')

class A2(Test):
    def __init__(self):
        print('enter A2')
        super().__init__()
        print('leave A2')

class B(A1,Test1):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')

class C(A2,Test2,A1):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')

class D(B,C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


print(D.mro())


'''
抽象类：@abstractmethod装饰器，只用来定义一些基本元素。一种生下来就是要做父类的特殊类，一旦对象化就会报错(Can't instantiate abstract class Entity with abstract methods
       get_title, set_title)。子类必须重写抽象类的含糊才能使用抽象函数，从而实现定义接口，自上而下的设计风范
'''

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self,title):
        pass

class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self,title):
        self.title=title

document=Document()
document.set_title('hello everyone')
print(document.get_title())


entity=Entity()