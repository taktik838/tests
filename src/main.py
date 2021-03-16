import unittest

from tests import check_left_bt
    
tests = unittest.TestLoader().loadTestsFromTestCase(check_left_bt.Check_left_buttons)

unittest.TextTestRunner().run(unittest.TestCase())