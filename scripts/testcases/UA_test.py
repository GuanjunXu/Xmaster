from uiautomator import device as d
import unittest
import time

class CancelAddingContact(unittest.TestCase):
    def setUp(self):
        super(CancelAddingContact,self).setUp()

    def testCancelAddContact(self):
        #Launch Contacts
        d(text = 'People').click.wait()
        assert d(description = 'Favorites').wait.exists(timeout = 2000), 'Contacts launch failed'

        #Tap on add contact icon
        d(description = 'Add Contact').click.wait()
        assert d(description = 'contact photo').wait.exists(timeout = 2000), 'Add contact page does not pop up'

        #Cancel adding contact
        d(description = 'More options').click.wait()
        assert d(text = 'Join').wait.exists(timeout = 2000), 'Menu does not pop up'

        d(text = 'Discard').click.wait()
        assert d(description = 'Favorites').wait.exists(timeout = 2000), 'Contacts launch failed'

        #Exit activity
        d.press.back()
        d.press.back()

        assert d(text = 'People').wait.exists(timeout = 2000), 'Contacts does not exit in 2s'

    def tearDown(self):
        super(CancelAddingContact,self).tearDown()

if __name__ == '__main__':
    unittest.main()
