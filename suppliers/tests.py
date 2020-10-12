from django.test import TestCase
import unittest

from suppliers.laskin import plus, plus_complicated

class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus(7, 2), 9)
        self.assertEqual(plus(7.20, 2.70), 9.90)
        self.assertEqual(plus(-7, 2), -5)

    def test_plus_complicated(self):
        # testaa ehdollisen yhteenlaskun toimivuus
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 8), 8)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, '2'), '9')
        self.assertEqual(plus(7, '2'), 9)
        self.assertEqual(plus('7', '2'), '9')
        self.assertEqual(plus(7.1, 2.1), 9.2)

    # TDD - Test Driven Development
    '''testi, toiminto, refaktotointi, testi, ... uudistus, testi'''
