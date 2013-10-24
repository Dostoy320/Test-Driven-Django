from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy fancy cheeses" into a text box.
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)
		# When she hits enter, the page updates and now lists:
		# "1. Buy fancy cheeses" as an item in the to-do list.

		# There is still a text box inviting her to enter another item.
		# Jeni adds "buy a case of wine" to the list.

		self.fail('Finish the test!')

		# The page updates again and now shows both items on her list.

 		# The site has generated a unique url, with text explaining its existence.

		# She visits the url, and her list is there.

		# Satisfied, she goes to do something else.

if __name__=='__main__':
	unittest.main(warnings='ignore')

