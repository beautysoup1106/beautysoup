import pytest

class TestLoginCase(object):

    def test01(self):
        print('test01')
        assert 1==2

    def test02(self):
        print('test02')
        assert 1==1

# 1if __name__ == '__main__':
#     pytest.main(['-sv','test01.py'])