from unittest import TestCase


class TestCalc_recruiters_value(TestCase):
    def test_calc_recruiters_value(self):
        from rule import calc_recruiters_value
        from gangster import Accountants, Brutes, Mercenaries, Famiglia

        self.assertEqual(('Accountants', 1), calc_recruiters_value((Accountants(0), Accountants(0))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Accountants(1))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Accountants(2), Accountants(2))))
        self.assertEqual(('Accountants', 4), calc_recruiters_value((Accountants(3), Accountants(3))))

        self.assertEqual(('Brutes', 1), calc_recruiters_value((Brutes(0), Brutes(0))))
        self.assertEqual(('Brutes', 2), calc_recruiters_value((Brutes(1), Brutes(1))))
        self.assertEqual(('Brutes', 3), calc_recruiters_value((Brutes(2), Brutes(2))))
        self.assertEqual(('Brutes', 4), calc_recruiters_value((Brutes(3), Brutes(3))))

        self.assertEqual(('Mercenaries', 1), calc_recruiters_value((Mercenaries(0), Mercenaries(0))))
        self.assertEqual(('Mercenaries', 2), calc_recruiters_value((Mercenaries(1), Mercenaries(1))))
        self.assertEqual(('Mercenaries', 3), calc_recruiters_value((Mercenaries(2), Mercenaries(2))))
        self.assertEqual(('Mercenaries', 4), calc_recruiters_value((Mercenaries(3), Mercenaries(3))))

        self.assertEqual(('Famiglia', 1), calc_recruiters_value((Famiglia(0), Famiglia(0))))
        self.assertEqual(('Famiglia', 2), calc_recruiters_value((Famiglia(1), Famiglia(1))))
        self.assertEqual(('Famiglia', 3), calc_recruiters_value((Famiglia(2), Famiglia(2))))
        self.assertEqual(('Famiglia', 4), calc_recruiters_value((Famiglia(3), Famiglia(3))))

    def test_calc_recruiters_value_with_mercenaries(self):
        from rule import calc_recruiters_value
        from gangster import Accountants, Brutes, Mercenaries, Famiglia

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(0), Mercenaries(0))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Accountants(0), Mercenaries(1))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Accountants(0), Mercenaries(2))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Accountants(0), Mercenaries(3))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Accountants(0), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(1), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(1), Mercenaries(1))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(2))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(3))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(2))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Accountants(2), Mercenaries(3))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Accountants(2), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(2))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(3), Mercenaries(3))))
        self.assertEqual(('Accountants', 4), calc_recruiters_value((Accountants(3), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(0), Accountants(0))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Mercenaries(1), Accountants(0))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Mercenaries(2), Accountants(0))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Mercenaries(3), Accountants(0))))
        self.assertEqual(('Accountants', 1), calc_recruiters_value((Mercenaries(4), Accountants(0))))

        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(0), Accountants(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(1), Accountants(1))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Mercenaries(2), Accountants(1))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Mercenaries(3), Accountants(1))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Mercenaries(4), Accountants(1))))

        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(0), Accountants(2))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(1), Accountants(2))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(2), Accountants(2))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Mercenaries(3), Accountants(2))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Mercenaries(4), Accountants(2))))

        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(0), Accountants(3))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(1), Accountants(3))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(2), Accountants(3))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(3), Accountants(3))))
        self.assertEqual(('Accountants', 4), calc_recruiters_value((Mercenaries(4), Accountants(3))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(1), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(1), Mercenaries(1))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(2))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(3))))
        self.assertEqual(('Accountants', 2), calc_recruiters_value((Accountants(1), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(2))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Accountants(2), Mercenaries(3))))
        self.assertEqual(('Accountants', 3), calc_recruiters_value((Accountants(2), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(0))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(2), Mercenaries(2))))
        self.assertEqual(('', 0), calc_recruiters_value((Accountants(3), Mercenaries(3))))
        self.assertEqual(('Accountants', 4), calc_recruiters_value((Accountants(3), Mercenaries(4))))

        self.assertEqual(('Brutes', 1), calc_recruiters_value((Brutes(0), Mercenaries(1))))
        self.assertEqual(('Brutes', 2), calc_recruiters_value((Brutes(1), Mercenaries(2))))
        self.assertEqual(('Brutes', 3), calc_recruiters_value((Brutes(2), Mercenaries(3))))
        self.assertEqual(('Brutes', 4), calc_recruiters_value((Brutes(3), Mercenaries(4))))

        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(0), Mercenaries(1))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(1), Mercenaries(2))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(2), Mercenaries(3))))
        self.assertEqual(('', 0), calc_recruiters_value((Mercenaries(3), Mercenaries(4))))

        self.assertEqual(('Famiglia', 1), calc_recruiters_value((Famiglia(0), Mercenaries(1))))
        self.assertEqual(('Famiglia', 2), calc_recruiters_value((Famiglia(1), Mercenaries(2))))
        self.assertEqual(('Famiglia', 3), calc_recruiters_value((Famiglia(2), Mercenaries(3))))
        self.assertEqual(('Famiglia', 4), calc_recruiters_value((Famiglia(3), Mercenaries(4))))
