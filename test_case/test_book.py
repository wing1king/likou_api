from get_token import *


class MyTestCase(unittest.TestCase):
    """阅读进度"""

    def setUp(self):
        self.book_id = 129337698467840
        self.user_id = 99999999999
        self.reason_id = 4


    def test_report(self):
        """投拆"""
        data = data
        res = requests.post(url= base_url + "/app/user/report",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_login(self):
        """登录/注册"""
        data = {
	        "book_id": self.book_id,
	        "chapter_id": self.chapter_id,
	        "cmd_id": self.cmd_id,
	        "option_id": self.option_id
	        }
        res = requests.post(url= base_url + "/app/user/login",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_refresh_token(self):
        """刷新token"""
        data = {
	        "access_token": get_token()
            }
        res = requests.post(url= base_url + "/app/user/refresh-token",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_black_list(self):
        """屏蔽用户"""
        data = {
	        "report_user_id": 2264982076
	        }    
        res = requests.post(url= base_url + "/app/add-black-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_books(self):
        """书本列表"""
        data = {
	        "page_num": 1,
	        "page_size": 5
            }
        res = requests.post(url= base_url + "/app/user/books",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_profile(self):
        """设置个人数据"""
        data = {
	        "nick_name": "wingking",
            "desc": "",
            "avatar": "https://xms-dev-1251001060.cos.ap-guangzhou.myqcloud.com/2019/09/1568086837108.jpg"
            }
        res = requests.post(url= base_url + "/app/user/edit-profile",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_profile(self):
        """获取个人页数据"""
        data = {
	        "user_id": self.user_id,
            }
        res = requests.post(url= base_url + "/app/user/get-profile",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)    

    def test_get_black_list(self):
        """获取黑名单列表"""
        data = {
	        "page_num": 1,
	        "page_size": 5
            }
        res = requests.post(url= base_url + "/app/user/get-black-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)   

    def test_add_black_list(self):
        """将用户加入黑名单"""
        data = {
	        "report_user_id": self.user_id
            }
        res = requests.post(url= base_url + "/app/user/add-black-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_cancel_black_list(self):
        """将用户移出黑名单"""
        data = {
	        "report_user_id": self.user_id
            }
        res = requests.post(url= base_url + "/app/user/cancel-black-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)        

    def test_get_black_list(self):
        """获取黑名单中指定用户"""
        data = {
	        "report_user_id": self.user_id
            }
        res = requests.post(url= base_url + "/app/user/get-black-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_cos_auth(self):
        """获取COS临时参数"""
        res = requests.post(url= base_url + "/app/user/get-cos-auth",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
