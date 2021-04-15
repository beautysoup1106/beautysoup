import pytest

class TestCase01(object):


    @classmethod
    def setup_class(cls):
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')
    def setup(self):

        print('setup')
    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')


    def teardown(self):
        print('teardown')
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

def test1():
    print('test1')

    print('test2')


def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

if __name__ == '__main__':
    pytest.main(['-vs','test07.py'])