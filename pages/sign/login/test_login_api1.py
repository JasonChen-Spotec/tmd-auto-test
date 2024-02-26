import allure
import pytest
from utils.restClient import RequestClient
from cases.sign.login import dataCases

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("交易端登录接口")
class TestLoginPageAPI:
    @pytest.mark.usefixtures("run_test")
    @allure.story("登录账号格式错误 生成环境不要执行")
    def testLoginCase1(self):
        # res = RequestClient.post(
        #     path="/api/h5/user/check/account",
        #     data=dataCases["casesList"][0]['data'],
        # )
        # exceptResult = dataCases['casesList'][0]['expected']
        # resData = res["header"]
        # del resData["traceId"]
        assert 2==3
        # assert resData == exceptResult
    @allure.story("登录账号不存在 生成环境要执行")
    def testLoginCase2(self):
        # res = RequestClient.post(
        #     path="/api/h5/user/check/account",
        #     data=dataCases["casesList"][1]['data'],
        # )
        # exceptResult = dataCases['casesList'][1]['expected']
        # resData = res["header"]
        # del resData["traceId"]
        assert 1==1
        # assert resData == exceptResult
    # @allure.story("黑名单账号")
    # def testLoginCase3(self):
    #     res = RequestClient.post(
    #         path="/api/h5/user/check/account",
    #         data=dataCases["casesList"][2]['data'],
    #     )
    #     exceptResult = dataCases['casesList'][2]['expected']
    #     resData = res["header"]
    #     del resData["traceId"]

    #     assert resData == exceptResult
    # @allure.story("登录账号为空")
    # def testLoginCase4(self):
    #     res = RequestClient.post(
    #         path="/api/h5/user/check/account",
    #         data=dataCases["casesList"][3]['data'],
    #     )
    #     exceptResult = dataCases['casesList'][3]['expected']
    #     resData = res["header"]
    #     del resData["traceId"]

    #     assert resData == exceptResult
    # @allure.story("登录密码不正确")
    # def testLoginCase5(self):
    #     res = RequestClient.post(
    #         path="/api/h5/user/check/account",
    #         data=dataCases["casesList"][4]['data'],
    #     )
    #     exceptResult = dataCases['casesList'][4]['expected']
    #     resData = res["header"]
    #     del resData["traceId"]

    #     assert resData == exceptResult
    # @allure.story("登录密码为空")
    # def testLoginCase6(self):
    #     res = RequestClient.post(
    #         path="/api/h5/user/check/account",
    #         data=dataCases["casesList"][5]['data'],
    #     )
    #     exceptResult = dataCases['casesList'][5]['expected']
    #     resData = res["header"]
    #     del resData["traceId"]

    #     assert resData == exceptResult
    # @allure.story("登录成功-密码登录")
    # def testLoginCase7(self):
    #     res = RequestClient.post(
    #         path="/api/h5/user/check/account",
    #         data=dataCases["casesList"][6]['data'],
    #     )
    #     exceptResult = dataCases['casesList'][6]['expected']
    #     resData = res["header"]
    #     del resData["traceId"]

    #     assert resData == exceptResult

