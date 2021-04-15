import pytest



@pytest.fixture()
def init():
    print('init.....')
    return 1


def test01(init):

    print('test01')


def test02(init):

    print('test02')


if __name__ == '__main__':
    pytest.main(['-sv','test06.py'])