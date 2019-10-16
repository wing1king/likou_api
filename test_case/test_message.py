from get_token import *


class MyTestCase(unittest.TestCase):
    """通知消息"""

    def setUp(self):
        pass

    def test_msg(self):
        """消息"""
        data = {	
	        "page_num": 1,
	        "page_size": 5
	        }
        res = requests.post(url= base_url + "/app/message/msg",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_news(self):
        """通知"""
        res = requests.post(url= base_url + "/app/message/news",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_moment(self):
        """动态"""
        data = {
	        "moment_type": 1,
	        "min_moment_id": 1,
	        "page_num": 1,
	        "page_size": 5
	        }
        res = requests.post(url= base_url + "/app/message/moment",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_update_msg(self):
        """更新消息已读"""
        data = {
	        "msg_id": 1
	        }        
        res = requests.post(url= base_url + "/app/message/news",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_update_moment(self):
        """更新动态已读"""
        data = {
	        "max_moment_id": 1
            }
        res = requests.post(url= base_url + "/app/message/update-moment",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
