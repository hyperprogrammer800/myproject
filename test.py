import unittest
import url_download

new_url = url_download.url

class TestUrl(unittest.TestCase):

	def test_download(self):
		result = url_download.download(new_url)
		self.assertEqual(result,'Success')
if __name__ == '__main__':
	unittest.main()
