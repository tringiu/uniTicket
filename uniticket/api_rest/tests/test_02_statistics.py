from django.contrib.auth import get_user_model
from django.test import TestCase



class uniTicketAPIStatsTest(TestCase):

    def setUp(self):
        self.op1 = get_user_model().objects.create(
            username = "operator"
        )
        self.user1 = get_user_model().objects.create(
            username = "test"
        )

    def test_result(self):
        pass