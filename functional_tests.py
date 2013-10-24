from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jeni visits the following url:
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do lists', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item straight away

		# She types "Buy fancy cheeses" into a text box.

		# When she hits enter, the page updates and now lists:
		# "1. Buy fancy cheeses" as an item in the to-do list.

		# There is still a text box inviting her to enter another item.
		# Jeni adds "buy a case of wine" to the list.

		# The page updates again and now shows both items on her list.

 		# The site has generated a unique url, with text explaining its existence.

		# She visits the url, and her list is there.

		# Satisfied, she goes to do something else.

if __name__=='__main__':
	unittest.main(warnings='ignore')

