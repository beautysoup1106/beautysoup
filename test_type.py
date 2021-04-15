import dis
'''
  6           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (('q', 'w', 'e'))
              8 BUILD_CONST_KEY_MAP      3
             10 RETURN_VALUE
 11           0 LOAD_GLOBAL              0 (dict)
              2 LOAD_CONST               1 (1)
              4 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              8 LOAD_CONST               4 (('q', 'w', 'e'))
             10 BUILD_CONST_KEY_MAP      3
             12 CALL_FUNCTION            1
             14 RETURN_VALUE
'''

'''
x+=1和x=x+1
    对于不可变类型，两者一样，没有区别
    对于可变类型，前者表示修改x自身的值，后者表示新创建一个’同名‘对象x，并将x+1赋值给新创建的同名变量
        x，之后，旧的x指向就会被释放。如x+=[4]等同于x.append(4),x=x+[4]则表示新创建一个列表，然后再重新指向x。
        set和dict不支持+=操作
'''


def make_dict():
    return {'q':1,'w':2,'e':3}


def make_dict2():

    return dict({'q':1,'w':2,'e':3})

dis.dis(make_dict)

dis.dis(make_dict2)