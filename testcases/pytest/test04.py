import pytest


@pytest.mark.do
def test01_add():
    print('test01_add')
@pytest.mark.undo
def test02_minus():
    print('test02_minus')

@pytest.mark.do
def test03_multi():
    print('test03_multi')
    assert 1==1
