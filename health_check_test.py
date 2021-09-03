#!/usr/bin/env python3

import unittest
import health_check

class Test_health_checks(unittest.TestCase):

    def Setup(self):

    def test_main_function(self):
        self.assertTrue(health_check.main())


    def test_hardware_errors(self):
        self.assertFalse(health_check.main())


if __name__== '__main__':
    unittest.main()
