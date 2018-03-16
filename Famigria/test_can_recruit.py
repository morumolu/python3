from unittest import TestCase


class TestCan_recruit(TestCase):
    def test_can_recruit(self):
        from rule import can_recruit
        from gangster import Accountants, Brutes, Mercenaries, Famiglia

        hand = {Accountants(0), Brutes(0), Mercenaries(0), Famiglia(0)}

        self.assertEqual(True, can_recruit(hand, Accountants(0)))
        hand.add(Accountants(0))

        self.assertEqual(True, can_recruit(hand, Accountants(1)))
        hand.add(Accountants(1))

        self.assertEqual(True, can_recruit(hand, Mercenaries(0)))
        hand.add(Mercenaries(0))

        self.assertEqual(True, can_recruit(hand, Mercenaries(1)))
        hand.add(Mercenaries(1))

        self.assertEqual(True, can_recruit(hand, Brutes(1)))
        hand.add(Brutes(1))

        self.assertEqual(True, can_recruit(hand, Famiglia(1), 1))

        self.assertEqual(True, can_recruit(hand, Accountants(2), 1))
