from get_token import *


class MyTestCase(unittest.TestCase):
    """阅读进度"""

    def setUp(self):
        self.book_id = 129337698467840
        self.chapter_id = 397
        self.cmd_id = 7064986742885395
        self.option_id = 1565674662000


    def test_vote(self):
        """用户投票"""
        data = {
	        "book_id": self.book_id,
	        "chapter_id": self.chapter_id,
	        "cmd_id": self.cmd_id,
	        "option_id": self.option_id
	        }
        res = requests.post(url= base_url + "/app/message/msg",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_news(self):
        """清除投票结果"""
        data = {
	        "book_id": self.book_id,
	        "chapter_id": self.chapter_id,
	        "cmd_id": self.cmd_id,
	        "option_id": self.option_id
	        }
        res = requests.post(url= base_url + "/app/message/news",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_moment(self):
        """获取投票结果数据"""
        data = {
	        "book_id": 127914029875200,
	        "chapter_id": 127914029883392,
	        "cmd_id": [127914054844416]
            }
        res = requests.post(url= base_url + "/app/message/moment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_clear_vote(self):
        """获取游戏存储数据"""
        data = {
	        "book_id":self.book_id,
	        "chapter_id":self.chapter_id,
	        "cmd_id":self.cmd_id
	        }    
        res = requests.post(url= base_url + "/app/play/clear-vote",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_set_data(self):
        """设置游戏存储数据"""
        data = {
	        "book_id": 70446320204544,
	        "data": {
		    "chapter-progress-362": 0
	            }
            }
        res = requests.post(url= base_url + "/app/play/set-data",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_data(self):
        """删除游戏存储数据"""
        data = {
	        "book_id": 70446320204544
            }
        res = requests.post(url= base_url + "/app/play/del-data",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)
    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
