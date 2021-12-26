from django.test import TestCase
from django.test.client import Client

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 1.1 포스트 목록 페이지를 가져온다.
        # 1.2 정상적으로 페이지가 로드된다.
        