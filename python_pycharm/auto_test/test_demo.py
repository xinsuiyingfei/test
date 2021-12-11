# import pytest
import pytest
import allure


@pytest.fixture(scope = 'class', autouse = True)
def front ( ) :
    print("类级别的前置条件")
    return "111"

@pytest.fixture(scope = 'class', autouse = True)
def after ( ) :
    yield after
    print("类级别的后置条件")
    return "222"


class Test01 :
    @allure.feature("测试一")
    def test_01 (self):
        print("执行测试一")
        assert 1==2,"预期结果不等于实际结果"

    @allure.feature("测试二")
    def test_02 (self, front) :
        assert front == 3, f"{front}结果不相等3"

    @allure.feature("测试三")
    def test_03 (self) :
        """test"""
        assert 'a' in 'abc', "结果不正确"
