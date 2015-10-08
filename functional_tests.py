from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Foo has head about a cool new online to-do app.
        # They go to check out it's homepage.
        self.browser.get('http://localhost:8000')

        # They notice the page title and header mention to-do lists.
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # They are invited to enter a to-do item straight away.

        # They type "buy peacockfeathers" into a text box (Foo's hobby
        # is tying fly-fishing lures).

if __name__ == '__main__':
    unittest.main(warnings='ignore')
