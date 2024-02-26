import pytest
from utils.logger import logger
from utils.restClient import RequestClient
import consts.env

def setup_module(module):
    print("Setup before module")


# 定义一个全局变量来存储 token
loginUserInfo = None


# @pytest.fixture(scope="session", autouse=True)
# def login_and_get_token():
#     # 在测试会话开始前请求登录接口，并获取 token
#     global loginUserInfo

#     res = RequestClient.post(
#         "/api/h5/user/check/account",
#         data={"account": "Lena.liu@spotec.net", "password": "abc123"},
#     )

#     if res['header']['code'] != '0000':
#       logger.info('Skipping tests because login failed')
#       pytest.skip("Skipping tests because login failed")

#     # 存全局登录信息
#     loginUserInfo = res['body']['appLoginVO']


@pytest.fixture
def run_test():
    if consts.env.baseHost =='pro':
        pytest.skip("Skipping test due to SKIP_TEST environment variable")

    yield
