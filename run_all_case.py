import sys
import time
import unittest
from imp import reload
from HTMLTestRunner import HTMLTestRunner
reload(sys)


# 定义测试用例的目录为当前目录
test_dir = 'E:\\test_platform_api\\test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = r'E:\test_platform_api\test_report\\' + now + '_test_teacher_result.html'

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="平台接口测试报告",
                            description="测试用例执行情况：")
    # 运行测试
    runner.run(discover)
    # 关闭报告文件
    fp.close()