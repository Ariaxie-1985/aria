import pytest

#id = [1,2,3]
@pytest.mark.incremental
class TestShop1(object):
    def test_1(self):
        global id1
        id1 =[1,2,3]



    def test_2(self):
        for id in id1:
            print(id)

# a = TestShop1()
# print(a.test_2())