import unittest

from 0-subs import number_of_subscribers

class TestNumberOfSubscribers(unittest.TestCase):
	def test_valid_subreddit(self):
		self.assertGreater(number_of_subscribers("python"), 0)

	def test_invalid_subreddit(self):
		self.assertEqual(number_of_subscribers("this_is_a_fake_subreddit"), 0)

if __name__ == '__main__':
	unittest.main()
